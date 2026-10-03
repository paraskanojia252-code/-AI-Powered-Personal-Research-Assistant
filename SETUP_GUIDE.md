# 🚀 AI Research Assistant - Setup & Deployment Guide

## 📋 Prerequisites
- Python 3.8+ installed on your system
- Google Gemini API Key (free tier available)
- Tavily API Key (free tier available)
- Git (for Streamlit Cloud deployment)

---

## 🔑 Getting API Keys

### 1️⃣ **Google Gemini API Key**
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikeys)
2. Click **"Create API Key"**
3. Copy the generated key (you'll need it for the app)
4. **Free tier:** 60 requests/minute ✅

### 2️⃣ **Tavily API Key**
1. Go to [Tavily API](https://tavily.com)
2. Sign up and create a free account
3. Copy your API key from the dashboard
4. **Free tier:** 100 API calls/month ✅

---

## 💻 Local Setup (Windows - No Admin Required)

### Step 1: Create a Project Folder
```bash
mkdir ai-research-assistant
cd ai-research-assistant
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create `.env` File (Optional - for local testing)
Create a file named `.env` in the project folder:
```
GEMINI_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### Step 5: Run the App Locally
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🌐 Deploy to Streamlit Cloud (Free)

### Step 1: Push Code to GitHub
1. Create a new GitHub repository
2. Push your project files:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-research-assistant.git
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to [Streamlit Cloud](https://share.streamlit.io)
2. Click **"New app"**
3. Select:
   - **GitHub repo:** ai-research-assistant
   - **Branch:** main
   - **Main file path:** app.py
4. Click **Deploy**

### Step 3: Add API Keys to Streamlit Cloud
1. Once deployed, click **⋮** (menu) → **Settings**
2. Go to **Secrets** section
3. Add your API keys in this format:
```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
TAVILY_API_KEY = "your_tavily_api_key_here"
```
4. Save and the app will automatically redeploy

---

## 🛠️ Project Structure

```
ai-research-assistant/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Local API keys (NOT for GitHub)
├── .gitignore            # Exclude .env from GitHub
└── SETUP_GUIDE.md        # This file
```

### Create `.gitignore` before pushing to GitHub:
```
.env
venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

---

## 📊 How the App Works

### Step 1: Web Search
- Fetches 5 relevant sources using **Tavily API**
- Displays sources with URLs and snippets

### Step 2: Content Extraction & Summarization
- Extracts text from each source URL
- Uses **Google Gemini** to create bullet-point summaries
- Tailored to your research question

### Step 3: Final Report Generation
- Synthesizes all summaries into one comprehensive report
- Uses Gemini to create a cohesive, well-structured analysis
- Professional, ready-to-use output

### Download Feature
- Export the complete report as a `.txt` file
- Includes all sources with URLs

---

## ⚙️ Configuration & Customization

### Change Number of Sources
In `app.py`, find this line:
```python
sources = fetch_sources(query, tavily_api_key, num_results=5)
```
Change `5` to any number (e.g., `10`)

### Adjust Content Extraction Length
In `app.py`, find:
```python
return text[:3000]  # Limit to 3000 chars
```
Increase to get more content (but costs more tokens)

### Change Summary Length
In the `summarize_content()` function, modify:
```python
Provide a concise bullet-point summary (3-5 key points)
```
Change `3-5` to your preferred range

### Change Final Report Length
In `generate_final_report()`, modify:
```python
Is written in clear, professional language (500-800 words)
```
Adjust the word count as needed

---

## 🐛 Troubleshooting

### ❌ "ModuleNotFoundError: No module named 'streamlit'"
**Solution:**
```bash
pip install streamlit
```

### ❌ "Invalid API Key"
**Solution:**
- Verify your API keys are correct
- Check there are no extra spaces in the key
- Ensure the key hasn't expired

### ❌ "No sources found"
**Solution:**
- Try a different research query
- Check your Tavily API quota
- Verify internet connection

### ❌ "Rate limit exceeded"
**Solution:**
- Wait a few minutes before making another request
- Upgrade your API plan if you hit limits frequently
- Consider reducing `num_results`

---

## 📈 API Costs

| Service | Free Tier | Cost |
|---------|-----------|------|
| **Gemini API** | 60 req/min | Free tier is generous |
| **Tavily API** | 100 calls/month | Then $0.01/call |

**Total Cost:** Essentially free for personal use! ✅

---

## 🚨 Important Notes

1. **Never commit `.env` file to GitHub** - Use Streamlit Secrets instead
2. **API keys in sidebar** - Users enter them in the app UI (no hardcoding)
3. **Token limits** - Very long articles may be truncated to save tokens
4. **Network speed** - First run takes ~30 seconds (API calls + processing)

---

## 📞 Support

If you encounter issues:
1. Check the **Troubleshooting** section above
2. Verify your API keys in the sidebar
3. Try a simpler research query
4. Check Streamlit logs: `streamlit run app.py` shows detailed errors

---

## 🎯 Next Steps

1. ✅ Get API keys (Gemini + Tavily)
2. ✅ Set up local environment
3. ✅ Test the app locally
4. ✅ Deploy to Streamlit Cloud
5. ✅ Share with friends!

---

**Happy Researching! 🔍📚**
