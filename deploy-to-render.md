# Deploy to Render - Step by Step Guide

## Prerequisites
- GitHub account with your code pushed
- Render account (free at render.com)

## Steps

### 1. Push Your Code to GitHub
```bash
git add .
git commit -m "Configure for Render deployment"
git push origin main
```

### 2. Create Render Account
- Go to [render.com](https://render.com)
- Sign up with GitHub

### 3. Deploy Your Service
- Click "New +" → "Web Service"
- Connect your GitHub repository
- Select the repository: `real-time-drawing-board-backend-deploy`
- Render will auto-detect it's a Python app

### 4. Configure Service
- **Name**: `drawing-board-backend` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `daphne -b 0.0.0.0 -p $PORT backend.asgi:application`
- **Plan**: Free

### 5. Environment Variables (Optional)
If you want to use Redis for WebSockets:
- Add `REDIS_URL` with your Redis connection string
- You can use Render's Redis service (free tier available)

### 6. Deploy
- Click "Create Web Service"
- Wait for build and deployment (usually 5-10 minutes)

### 7. Access Your App
- Your app will be available at: `https://your-app-name.onrender.com`

## Notes
- Free tier includes 750 hours/month
- App sleeps after 15 minutes of inactivity
- First request after sleep may take 30-60 seconds
- WebSockets work on free tier

## Troubleshooting
- Check build logs if deployment fails
- Ensure all requirements are in `requirements.txt`
- Verify `render.yaml` syntax
