# 🔍 AI-Powered Personal Research Assistant

An intelligent research automation tool that conducts web research, summarizes content from multiple sources, and generates comprehensive research reports using **Streamlit**, **Google Gemini**, and **Tavily API**.

## ✨ Features

✅ **Automated Web Research** - Search and fetch relevant sources automatically  
✅ **Smart Summarization** - AI-powered summaries for each source  
✅ **Comprehensive Reports** - Synthesized final analysis combining all sources  
✅ **User-Friendly UI** - Clean, intuitive Streamlit interface  
✅ **Report Export** - Download reports as text files  
✅ **Cloud Deployment** - Deployed on Streamlit Cloud (free)  

## 🚀 Quick Start

### Local Setup (3 minutes)

```bash
# 1. Clone or download the project
cd ai-research-assistant

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

Visit `http://localhost:8501` in your browser

### Get API Keys

1. **Gemini API** (free): [Google AI Studio](https://aistudio.google.com/app/apikeys)
2. **Tavily API** (free): [Tavily.com](https://tavily.com)

## 📋 How It Works

```
User Query
    ↓
[Step 1] Web Search (Tavily) → Find 5 relevant sources
    ↓
[Step 2] Content Extraction → Extract text from each URL
    ↓
[Step 3] AI Summarization (Gemini) → Create bullet-point summaries
    ↓
[Step 4] Final Report Generation → Synthesize all summaries
    ↓
Research Report + Sources → Ready to download/use
```

## 🌐 Live Demo

**Try it here:** [Coming Soon - Deploy to Streamlit Cloud]

## 📁 Project Structure

```
ai-research-assistant/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Dependencies
├── SETUP_GUIDE.md        # Detailed setup instructions
├── README.md             # This file
├── .gitignore            # Git ignore rules
└── secrets_template.toml # API keys template for Streamlit Cloud
```

## ⚙️ Configuration

### Environment Variables (Local)
Create `.env` file:
```
GEMINI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

### Streamlit Cloud Secrets
Add secrets via Streamlit Cloud UI → Settings → Secrets

## 🔧 Customization

### Change number of sources (default: 5)
Edit `app.py`:
```python
sources = fetch_sources(query, tavily_api_key, num_results=10)
```

### Adjust content extraction length
```python
return text[:3000]  # Increase for more content
```

### Modify report length
Change word count in final report prompt (default: 500-800 words)

## 📊 API Usage & Costs

| API | Free Tier | Cost |
|-----|-----------|------|
| Google Gemini | 60 req/min | ✅ Free |
| Tavily | 100 calls/month | ✅ Free (then $0.01/call) |

**Total: FREE for personal research!** 💰

## 🐛 Troubleshooting

### "No sources found"
- Try a different research query
- Check internet connection
- Verify Tavily API key

### "Invalid API Key"
- Double-check API key in sidebar
- Ensure no extra spaces
- Regenerate key if needed

### "Rate limit exceeded"
- Wait a few minutes
- Upgrade API plan if needed
- Reduce number of sources

See `SETUP_GUIDE.md` for more help.

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free)

1. Push code to GitHub
2. Sign in to [Streamlit Cloud](https://share.streamlit.io)
3. Click **"New app"**
4. Select your GitHub repo and `app.py`
5. Add API keys in **Secrets**
6. Deploy! 🎉

**Full instructions in SETUP_GUIDE.md**

## 📚 Dependencies

- **streamlit** - Web UI framework
- **requests** - HTTP library for web scraping
- **google-generativeai** - Google Gemini API client
- **python-dotenv** - Environment variable management

## 💡 Example Use Cases

- **Research Papers** - Find latest papers on a topic
- **Market Analysis** - Gather competitive intelligence
- **News Aggregation** - Summarize latest news on a topic
- **Learning** - Quick research for educational purposes
- **Decision Making** - Gather info before making decisions

## 🔐 Security Notes

⚠️ **Never commit API keys to GitHub**  
✅ Use `.env` locally (file is in `.gitignore`)  
✅ Use Streamlit Secrets for cloud deployment  
✅ Keys are never logged or stored  

## 📝 License

This project is open source. Feel free to modify and use!

## 🤝 Contributing

Have ideas to improve this? Feel free to:
- Fork the repository
- Create a feature branch
- Submit a pull request

## 📞 Support

Need help?
1. Check `SETUP_GUIDE.md` for detailed instructions
2. Review troubleshooting section
3. Check API documentation:
   - [Gemini API Docs](https://ai.google.dev/)
   - [Tavily API Docs](https://tavily.com)

## 🎯 Future Enhancements

- [ ] PDF research papers support
- [ ] Multi-language summaries
- [ ] Citation formatting (APA, MLA)
- [ ] Markdown export
- [ ] Research history/saved queries
- [ ] Interactive source filtering

---

**Made with ❤️ using Python, Streamlit, and AI**

Happy researching! 🔍📚
