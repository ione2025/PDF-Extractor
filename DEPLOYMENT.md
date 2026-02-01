# 🚀 Web Deployment Guide - PDF Extractor Pro

This guide explains how to deploy PDF Extractor Pro as a production web application.

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Development Setup](#development-setup)
- [Production Deployment](#production-deployment)
- [Deployment Platforms](#deployment-platforms)
- [Environment Configuration](#environment-configuration)
- [Troubleshooting](#troubleshooting)

## ⚡ Quick Start

### Run as Web Application (Development)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the web application
python app.py
```

Then open your browser and go to: **http://localhost:5000**

The application runs as a web service without auto-opening browsers.

### Run with Environment Variables

```bash
# Set configuration
export FLASK_DEBUG=False
export PORT=8080
export GEMINI_API_KEY=your_api_key_here

# Run the application
python app.py
```

## 🛠️ Development Setup

### 1. Clone and Install

```bash
git clone https://github.com/ione2025/PDF-Extractor.git
cd PDF-Extractor
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings
nano .env
```

### 3. Install System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr poppler-utils
sudo apt-get install tesseract-ocr-ara tesseract-ocr-chi-tra tesseract-ocr-chi-sim
```

**macOS:**
```bash
brew install tesseract poppler tesseract-lang
```

**Windows:**
- Install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
- Install Poppler: https://github.com/oschwartz10612/poppler-windows/releases

### 4. Run Development Server

```bash
python app.py
```

Access at: http://localhost:5000

## 🌐 Production Deployment

### Using Gunicorn (Recommended for Production)

#### 1. Install Gunicorn

```bash
pip install gunicorn
```

#### 2. Run with Gunicorn

```bash
# Basic usage
gunicorn wsgi:app

# Production configuration (4 workers)
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

# With timeout settings (for long PDF processing)
gunicorn -w 4 -b 0.0.0.0:5000 --timeout 300 wsgi:app

# With logging
gunicorn -w 4 -b 0.0.0.0:5000 --access-logfile - --error-logfile - wsgi:app
```

### Using Waitress (Windows-friendly)

```bash
# Install Waitress
pip install waitress

# Run with Waitress
waitress-serve --host=0.0.0.0 --port=5000 wsgi:app
```

## 🌍 Deployment Platforms

### Heroku

1. **Create Procfile:**
```
web: gunicorn wsgi:app
```

2. **Deploy:**
```bash
heroku create pdf-extractor-pro
heroku config:set GEMINI_API_KEY=your_api_key
git push heroku main
```

### Docker

1. **Create Dockerfile:**
```dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-ara \
    tesseract-ocr-chi-tra \
    tesseract-ocr-chi-sim \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .
RUN mkdir -p uploads output

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--timeout", "300", "wsgi:app"]
```

2. **Build and run:**
```bash
docker build -t pdf-extractor-pro .
docker run -p 5000:5000 -e GEMINI_API_KEY=your_key pdf-extractor-pro
```

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - FLASK_DEBUG=False
    volumes:
      - ./uploads:/app/uploads
      - ./output:/app/output
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

## ⚙️ Environment Configuration

### Environment Variables

Create a `.env` file or set in your deployment platform:

```bash
# Flask Configuration
FLASK_DEBUG=False
HOST=0.0.0.0
PORT=5000

# API Keys
GEMINI_API_KEY=your_gemini_api_key_here

# File Upload Settings
MAX_CONTENT_LENGTH=52428800  # 50MB
```

## 🔧 Web Server Options

### Nginx Reverse Proxy

Configure Nginx as a reverse proxy:

```nginx
server {
    listen 80;
    server_name your-domain.com;
    client_max_body_size 50M;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_connect_timeout 300s;
        proxy_send_timeout 300s;
        proxy_read_timeout 300s;
    }
}
```

### Systemd Service (Linux)

Create `/etc/systemd/system/pdf-extractor.service`:

```ini
[Unit]
Description=PDF Extractor Pro Web Application
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/PDF-Extractor
Environment="PATH=/var/www/PDF-Extractor/venv/bin"
Environment="GEMINI_API_KEY=your_api_key_here"
ExecStart=/var/www/PDF-Extractor/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 --timeout 300 wsgi:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable pdf-extractor
sudo systemctl start pdf-extractor
```

## 🐛 Troubleshooting

### Port already in use

```bash
# Find process using port 5000
lsof -i :5000
```

### Module not found

```bash
pip install -r requirements.txt
```

### Tesseract not found

```bash
# Ubuntu
sudo apt-get install tesseract-ocr
# Verify
tesseract --version
```

## 🔒 Security Checklist

- [ ] Set `FLASK_DEBUG=False` in production
- [ ] Use environment variables for secrets
- [ ] Set up HTTPS (SSL/TLS)
- [ ] Configure firewall rules
- [ ] Set file upload limits
- [ ] Regular security updates

## 📊 Health Check

The application includes a health check endpoint:

```bash
curl http://localhost:5000/health
# Response: {"status": "healthy"}
```

---

**Your PDF Extractor Pro is now ready for web deployment! 🎉**
