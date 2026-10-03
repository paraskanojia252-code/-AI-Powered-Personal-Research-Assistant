# ⚡ Quick Reference Guide

## 🚀 Start the App (2 steps)

### Windows (No Admin Needed)
```bash
venv\Scripts\activate
streamlit run app.py
```

### Mac/Linux
```bash
source venv/bin/activate
streamlit run app.py
```

Then open: `http://localhost:8501`

---

## 🔑 Get API Keys (5 minutes)

### Gemini API (FREE)
1. Go: https://aistudio.google.com/app/apikeys
2. Click: "Create API Key"
3. Copy: The generated key
4. Paste: In the app's sidebar

### Tavily API (FREE)
1. Go: https://tavily.com
2. Sign up
3. Copy: API key from dashboard
4. Paste: In the app's sidebar

---

## 📊 How the Research Works

```
Your Question
    ↓
TAVILY SEARCH → Finds 5 relevant sources + URLs
    ↓
CONTENT EXTRACTION → Downloads text from each URL
    ↓
GEMINI SUMMARIZATION → Creates 3-5 point summary per source
    ↓
GEMINI SYNTHESIS → Combines all summaries into 1 report
    ↓
Your Research Report ✓
```

---

## 🎯 Using the App

1. **Enter Question** - Type your research query
2. **Enter API Keys** - Paste them in the sidebar
3. **Click "Start Research"** - Watch the progress
4. **View Results** - Sources → Summaries → Final Report
5. **Download** - Get the complete report as .txt

**Time taken:** ~30 seconds per research query

---

## 📊 Project Structure Explained

```
app.py
  ├── fetch_sources()          [Step 1: Search with Tavily]
  ├── extract_content_from_url() [Get text from URLs]
  ├── summarize_content()      [Step 2: Summarize with Gemini]
  └── generate_final_report()  [Step 3: Synthesize with Gemini]

requirements.txt
  ├── streamlit          [Web UI]
  ├── requests           [HTTP requests]
  ├── google-generativeai [Gemini API]
  └── python-dotenv      [Environment vars]
```

---

## 🛠️ Most Common Changes

### Want more sources?
Edit `app.py`, line with:
```python
sources = fetch_sources(query, tavily_api_key, num_results=5)
```
Change `5` → `10`

### Want longer summaries?
Edit the prompt in `summarize_content()`:
```python
Provide a concise bullet-point summary (3-5 key points)
```
Change to `(5-8 key points)`

### Want different final report length?
Edit the prompt in `generate_final_report()`:
```python
(500-800 words)
```
Change to your preferred length

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "ModuleNotFoundError" | Run: `pip install -r requirements.txt` |
| "Invalid API Key" | Check key in sidebar (no spaces/typos) |
| "No sources found" | Try different query / check internet |
| "Rate limit" | Wait 5 mins / reduce num_results |
| App won't start | Verify Python version: `python --version` |

---

## 💾 Save Your Work

### Export Report
- Click **"Download Report as Text"** button
- Saves as: `research_report_YYYYMMDD_HHMMSS.txt`

### Keep Sources
- Screenshot or copy the sources section
- All URLs are clickable in the UI

---

## 🌐 Deploy to Cloud (Free)

### On Streamlit Cloud in 5 minutes:

1. Push to GitHub:
```bash
git add .
git commit -m "Initial commit"
git push
```

2. Go to https://share.streamlit.io
3. Click "New app"
4. Select your GitHub repo
5. Enter `app.py` as main file
6. In Settings → Secrets, add:
```toml
GEMINI_API_KEY = "your_key"
TAVILY_API_KEY = "your_key"
```
7. Deploy!

**Your app is now live and shareable!** 🎉

---

## 📈 API Limits & Costs

```
Gemini API:
├── Free: 60 requests per minute ✅
└── Cost: $0 for personal research

Tavily API:
├── Free: 100 searches per month ✅
└── Cost: $0 for basic research
```

**Total for typical use: FREE!** 💰

---

## 📚 Example Queries to Try

1. "What are latest AI developments in 2024?"
2. "How does quantum computing work?"
3. "Best practices for remote team management"
4. "Climate change solutions being implemented"
5. "History and evolution of Python programming"

---

## 🔐 Security Checklist

- ✅ Never put API keys in code
- ✅ Use `.env` locally (in `.gitignore`)
- ✅ Use Streamlit Secrets for cloud
- ✅ Don't share `secrets_template.toml` with actual keys
- ✅ Regenerate keys if accidentally exposed

---

## 📞 Need Help?

1. **Local Issues** → Run: `streamlit run app.py --logger.level=debug`
2. **API Issues** → Check rate limits in their dashboards
3. **Deployment Issues** → See SETUP_GUIDE.md
4. **General Help** → Read README.md

---

## ⚡ Pro Tips

💡 Use specific queries for better results  
💡 Same query = same results (no extra API calls)  
💡 Reports are saved in session (download before refresh)  
💡 Tavily limits: plan 2-3 research per day with free tier  

---

## 🎓 What You'll Learn

By using this project, you'll understand:
- Web scraping & APIs
- LLM integration (Gemini)
- Streamlit for web apps
- Python best practices
- Cloud deployment
- Working with AI pipelines

---

**Happy Researching! 🔍**
