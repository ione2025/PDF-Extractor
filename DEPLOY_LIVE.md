# 🚀 Deploy Your Own Live Website - PDF Extractor Pro

Get your own live website URL in minutes! No coding or local setup required.

## ⚡ Quick Deploy (Recommended)

### Option 1: Deploy to Render (FREE) ⭐

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/ione2025/PDF-Extractor)

**Steps:**
1. Click the "Deploy to Render" button above
2. Sign in with your GitHub account (free)
3. Click "Create Web Service"
4. Wait 5-10 minutes for deployment
5. Get your live URL: `https://pdf-extractor-pro.onrender.com`

**Features:**
- ✅ FREE forever
- ✅ Automatic deployment from GitHub
- ✅ Auto-restart on crashes
- ✅ HTTPS included
- ⚠️ Sleeps after 15 min of inactivity (wakes up when accessed)

### Option 2: Deploy to Railway (FREE) ⭐

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/6JwSne?referralCode=alphasec)

**Steps:**
1. Click the "Deploy on Railway" button above
2. Sign in with your GitHub account (free)
3. Click "Deploy Now"
4. Wait 3-5 minutes for deployment
5. Get your live URL from Railway dashboard

**Features:**
- ✅ FREE $5 credit monthly (enough for this app)
- ✅ Always on (doesn't sleep)
- ✅ Fast deployment
- ✅ HTTPS included

### Option 3: Deploy to Heroku

**Steps:**
1. Fork this repository to your GitHub account
2. Sign up at [Heroku.com](https://heroku.com) (free)
3. Create a new app
4. Connect to your GitHub repository
5. Enable automatic deploys
6. Add environment variable: `GEMINI_API_KEY=AIzaSyDLumkxN_6uKWwqJKs5QwOT8jP9sGCW0hQ`
7. Deploy!

**Or use Heroku CLI:**
```bash
# Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
heroku login
heroku create pdf-extractor-pro
heroku config:set GEMINI_API_KEY=AIzaSyDLumkxN_6uKWwqJKs5QwOT8jP9sGCW0hQ
git push heroku main
```

Your app will be at: `https://pdf-extractor-pro.herokuapp.com`

### Option 4: Deploy to Fly.io (FREE)

```bash
# Install Fly CLI: https://fly.io/docs/hands-on/install-flyctl/
fly auth signup
fly launch
fly deploy
```

## 🐳 Docker Deployment

### Deploy Anywhere with Docker

```bash
# Build and run locally
docker-compose up -d

# Or using Docker directly
docker build -t pdf-extractor .
docker run -p 5000:5000 -e GEMINI_API_KEY=AIzaSyDLumkxN_6uKWwqJKs5QwOT8jP9sGCW0hQ pdf-extractor
```

### Deploy to Any Cloud Provider

The Docker image works on:
- AWS ECS/Fargate
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform
- Any VPS with Docker

## 📋 Deployment Files Included

This repository includes deployment configurations for:

- ✅ `Procfile` - Heroku deployment
- ✅ `render.yaml` - Render.com deployment
- ✅ `railway.json` - Railway.app deployment
- ✅ `Dockerfile` - Container deployment
- ✅ `docker-compose.yml` - Local Docker deployment
- ✅ `wsgi.py` - Production WSGI server

## 🔧 Configuration

### Environment Variables

All platforms need this environment variable:

```
GEMINI_API_KEY=AIzaSyDLumkxN_6uKWwqJKs5QwOT8jP9sGCW0hQ
```

Optional variables:
```
FLASK_DEBUG=False
PORT=5000
HOST=0.0.0.0
```

## ✅ Verification

After deployment, verify your app is working:

1. Visit your app URL
2. Check health endpoint: `https://your-app.com/health`
3. You should see: `{"status": "healthy"}`

## 🆓 Cost Comparison

| Platform | Free Tier | Always On | Auto Deploy | HTTPS |
|----------|-----------|-----------|-------------|-------|
| Render | ✅ Yes | ⚠️ Sleeps | ✅ Yes | ✅ Yes |
| Railway | ✅ $5/month | ✅ Yes | ✅ Yes | ✅ Yes |
| Heroku | ✅ 550 hrs/mo | ⚠️ Sleeps | ✅ Yes | ✅ Yes |
| Fly.io | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

**Recommendation:** Use Railway or Render for best free experience.

## 🔒 Security Note

The Gemini API key is included in the deployment configs for convenience. For production use:

1. Generate your own API key at [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Set it as an environment variable in your deployment platform
3. Never commit API keys to public repositories

## 🐛 Troubleshooting

### App won't start
- Check deployment logs in your platform dashboard
- Verify `GEMINI_API_KEY` is set correctly
- Ensure all dependencies installed

### "Application Error" message
- Check if app is sleeping (Render/Heroku free tier)
- Wait 30 seconds and refresh
- Check health endpoint: `/health`

### API errors
- Verify Gemini API key is valid
- Check API quota hasn't been exceeded
- Try regenerating the API key

## 📞 Support

If you have deployment issues:
1. Check the platform's status page
2. Review deployment logs
3. Try redeploying
4. Open an issue on GitHub

---

**Get your live website URL now! Click a deploy button above! 🚀**
