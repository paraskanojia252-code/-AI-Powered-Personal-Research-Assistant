import os
import re
from datetime import datetime

import requests
import streamlit as st
import google.generativeai as genai


# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ------------------------------------------------------------
# Custom CSS
# ------------------------------------------------------------
st.markdown(
    """
    <style>
    .source-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 4px solid #3498db;
    }
    .summary-box {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 4px solid #4caf50;
    }
    .report-box {
        background-color: #fff3e0;
        padding: 20px;
        border-radius: 8px;
        margin: 15px 0;
        border-left: 4px solid #ff9800;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# Session state
# ------------------------------------------------------------
if "research_data" not in st.session_state:
    st.session_state.research_data = {
        "query": "",
        "sources": [],
        "summaries": [],
        "final_report": "",
        "status": "ready",
    }


# ------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------
st.sidebar.title("⚙️ Configuration")
st.sidebar.markdown("---")

gemini_api_key = st.sidebar.text_input(
    "🔑 Gemini API Key",
    type="password",
    key="gemini_key",
)

tavily_api_key = st.sidebar.text_input(
    "🔑 Tavily API Key",
    type="password",
    key="tavily_key",
)

if gemini_api_key:
    genai.configure(api_key=gemini_api_key)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    ### 📖 How to Use
    1. Enter your Gemini API key.
    2. Enter your Tavily API key.
    3. Type a research question.
    4. Click **Start Research**.
    5. Wait for sources and summaries.
    6. View or download the final report.
    """
)

st.sidebar.markdown("---")
st.sidebar.caption("🚀 Powered by Gemini + Tavily")


# ------------------------------------------------------------
# Title
# ------------------------------------------------------------
st.title("🔍 AI-Powered Personal Research Assistant")
st.markdown("*Automate your research with AI-powered summaries and insights*")
st.markdown("---")


# ------------------------------------------------------------
# Tavily source search
# ------------------------------------------------------------
def fetch_sources(query: str, api_key: str, num_results: int = 5):
    """Fetch research sources from Tavily."""
    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": api_key,
                "query": query,
                "max_results": num_results,
                "include_answer": False,
            },
            timeout=30,
        )
        response.raise_for_status()

        data = response.json()
        sources = []

        for result in data.get("results", []):
            sources.append(
                {
                    "title": result.get("title", "No Title"),
                    "url": result.get("url", ""),
                    "snippet": result.get(
                        "content",
                        result.get("snippet", "No snippet available"),
                    ),
                }
            )

        return sources

    except requests.RequestException as e:
        st.error(f"❌ Tavily request failed: {e}")
        return []
    except Exception as e:
        st.error(f"❌ Error fetching sources: {e}")
        return []


# ------------------------------------------------------------
# Extract webpage text
# ------------------------------------------------------------
def extract_content_from_url(url: str):
    """Download a webpage and perform basic HTML-to-text cleaning."""
    try:
        response = requests.get(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 Chrome/153.0 Safari/537.36"
                )
            },
            timeout=15,
        )
        response.raise_for_status()

        text = response.text
        text = re.sub(r"<script.*?</script>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<style.*?</style>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()

        return text[:5000]

    except Exception as e:
        return f"Could not extract content: {e}"


# ------------------------------------------------------------
# Gemini helper
# ------------------------------------------------------------
def get_gemini_model():
    """
    Uses a current Gemini model name instead of the old 'gemini-pro'
    name used in the original code.
    """
    if not gemini_api_key:
        raise ValueError("Gemini API key is missing.")

    return genai.GenerativeModel("gemini-1.5-flash")


def summarize_content(content: str, title: str, query: str):
    """Summarize one source with Gemini."""
    try:
        model = get_gemini_model()

        prompt = f"""
You are a research assistant.

Research question:
{query}

Article title:
{title}

Article content:
{content}

Summarize this source specifically in relation to the research question.

Return 3-5 concise bullet points.
Do not invent facts that are not supported by the provided content.
"""

        response = model.generate_content(prompt)

        if not response.text:
            return "No summary was returned by Gemini."

        return response.text

    except Exception as e:
        return f"Error summarizing source: {e}"


# ------------------------------------------------------------
# Final report
# ------------------------------------------------------------
def generate_final_report(query: str, summaries: list, sources: list):
    """Generate a cohesive research report from source summaries."""
    try:
        model = get_gemini_model()

        summaries_text = "\n\n".join(
            f"Source: {sources[i]['title']}\n{summaries[i]}"
            for i in range(min(len(summaries), len(sources)))
        )

        prompt = f"""
You are a research analyst.

Research question:
{query}

Below are summaries collected from multiple sources:

{summaries_text}

Create a clear, professional research report.

Requirements:
1. Directly answer the research question.
2. Synthesize information across the sources.
3. Highlight the major findings.
4. Mention uncertainty, limitations, or conflicting information when present.
5. Use clear headings and bullet points where useful.
6. Do not invent information.
7. Keep the report approximately 500-800 words.
"""

        response = model.generate_content(prompt)

        if not response.text:
            return "No final report was returned by Gemini."

        return response.text

    except Exception as e:
        return f"Error generating report: {e}"


# ------------------------------------------------------------
# Research interface
# ------------------------------------------------------------
col1, col2 = st.columns([3, 1])

with col1:
    query = st.text_input(
        "🔎 Enter Your Research Question:",
        placeholder="e.g., What are the latest developments in AI?",
        key="query_input",
    )

with col2:
    st.write("")
    research_button = st.button(
        "🚀 Start Research",
        use_container_width=True,
    )

st.markdown("---")


# ------------------------------------------------------------
# Research workflow
# ------------------------------------------------------------
if research_button:
    if not query.strip():
        st.error("❌ Please enter a research question.")

    elif not gemini_api_key.strip():
        st.error("❌ Please enter your Gemini API key in the sidebar.")

    elif not tavily_api_key.strip():
        st.error("❌ Please enter your Tavily API key in the sidebar.")

    else:
        st.session_state.research_data["query"] = query
        st.session_state.research_data["sources"] = []
        st.session_state.research_data["summaries"] = []
        st.session_state.research_data["final_report"] = ""

        # Step 1
        st.info("📡 Step 1: Fetching relevant sources...")
        sources = fetch_sources(query, tavily_api_key)

        if not sources:
            st.error("❌ No sources found. Please try a different query.")
        else:
            st.session_state.research_data["sources"] = sources
            st.success(f"✅ Found {len(sources)} sources!")

            # Step 2
            st.info("📝 Step 2: Summarizing sources...")
            summaries = []
            summary_placeholder = st.empty()

            for idx, source in enumerate(sources, start=1):
                summary_placeholder.write(
                    f"Processing source {idx}/{len(sources)}: "
                    f"**{source['title']}**"
                )

                content = extract_content_from_url(source["url"])
                summary = summarize_content(
                    content,
                    source["title"],
                    query,
                )
                summaries.append(summary)

            st.session_state.research_data["summaries"] = summaries
            summary_placeholder.empty()
            st.success("✅ All sources summarized!")

            # Step 3
            st.info("📊 Step 3: Generating final research report...")
            final_report = generate_final_report(
                query,
                summaries,
                sources,
            )

            st.session_state.research_data["final_report"] = final_report
            st.success("✅ Research complete!")


# ------------------------------------------------------------
# Display sources
# ------------------------------------------------------------
if st.session_state.research_data["sources"]:
    st.markdown("---")
    st.subheader("📋 Collected Sources")

    for idx, source in enumerate(
        st.session_state.research_data["sources"],
        start=1,
    ):
        st.markdown(
            f"""
            <div class="source-box">
                <strong>{idx}. {source['title']}</strong><br>
                <small>
                    🔗 <a href="{source['url']}" target="_blank">
                    {source['url']}
                    </a>
                </small><br>
                <em>{source['snippet']}</em>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ------------------------------------------------------------
# Display summaries
# ------------------------------------------------------------
if st.session_state.research_data["summaries"]:
    st.markdown("---")
    st.subheader("📝 Source-wise Summaries")

    for idx, summary in enumerate(
        st.session_state.research_data["summaries"]
    ):
        source_title = st.session_state.research_data["sources"][idx]["title"]

        with st.expander(f"📌 {source_title}", expanded=False):
            st.markdown(
                f"""
                <div class="summary-box">
                    {summary}
                </div>
                """,
                unsafe_allow_html=True,
            )


# ------------------------------------------------------------
# Display final report
# ------------------------------------------------------------
if st.session_state.research_data["final_report"]:
    st.markdown("---")
    st.subheader("📊 Final Research Report")

    st.markdown(
        f"""
        <div class="report-box">
            {st.session_state.research_data["final_report"]}
        </div>
        """,
        unsafe_allow_html=True,
    )

    report_text = f"""
RESEARCH REPORT
===============

Query: {st.session_state.research_data['query']}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

SOURCES:
{chr(10).join(
    f"{i + 1}. {s['title']} ({s['url']})"
    for i, s in enumerate(st.session_state.research_data['sources'])
)}

FINAL REPORT:
{st.session_state.research_data['final_report']}
"""

    st.download_button(
        label="📥 Download Report as Text",
        data=report_text,
        file_name=(
            f"research_report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        ),
        mime="text/plain",
    )
