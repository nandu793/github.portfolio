# SETUP INSTRUCTIONS - BM Music

Quick setup guide for getting BM Music running locally.

## Prerequisites
- Node.js v14+ (https://nodejs.org)
- MongoDB (local or MongoDB Atlas)
- Git
- Code Editor (VS Code recommended)

## Step-by-Step Setup

### 1. MongoDB Setup (Choose One)

#### Option A: Local MongoDB
```bash
# Windows
# Download and install from https://www.mongodb.com/try/download/community

# Mac
brew install mongodb-community
brew services start mongodb-community

# Linux (Ubuntu)
sudo apt-get install -y mongodb
sudo systemctl start mongod
```

#### Option B: MongoDB Atlas (Cloud)
1. Visit https://www.mongodb.com/cloud/atlas
2. Create free account
3. Create a cluster
4. Get connection string
5. Note it for later

### 2. Backend Setup

```bash
# Navigate to backend directory
cd SoundWave/backend

# Install dependencies
npm install

# Create .env file
cp .env.example .env
```

**Edit `.env` file with your values:**
```
PORT=5000
MONGODB_URI=mongodb://localhost:27017/soundwave
# OR for MongoDB Atlas:
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/soundwave

JWT_SECRET=your_secret_key_here
FRONTEND_URL=http://localhost:3000
GOOGLE_CLIENT_ID=skip_for_now
GOOGLE_CLIENT_SECRET=skip_for_now
GOOGLE_CALLBACK_URL=http://localhost:5000/api/auth/google/callback
SESSION_SECRET=your_session_key
```

**Seed sample data:**
```bash
node seed.js
```

Output should show:
```
✅ Admin user created
✅ 5 sample songs created
✅ Sample playlists created
🎵 Database seeding completed successfully!
```

**Start backend server:**
```bash
npm start
```

You should see:
```
🎵 BM Music Backend Server running on port 5000
```

### 3. Frontend Setup

Open new terminal/command prompt:

```bash
# Navigate to frontend
cd SoundWave/frontend

# Start local web server (choose one method)

# Method 1: Python 3
python -m http.server 3000

# Method 2: Python 2
python -m SimpleHTTPServer 3000

# Method 3: Node.js HTTP Server
npx http-server -p 3000

# Method 4: VS Code Live Server
# - Install "Live Server" extension
# - Right-click index.html → "Open with Live Server"
```

### 4. Access Application

Open browser and navigate to:
```
http://localhost:3000
```

## Login with Sample Account

**Email:** admin@bmmusic.com  
**Password:** password123

## Optional: Google OAuth Setup (For Production)

1. Go to https://console.cloud.google.com
2. Create new project named "BM Music"
3. Search for "OAuth consent screen"
4. Configure OAuth consent screen
5. Go to "Credentials"
6. Click "Create Credentials" → "OAuth 2.0 Client ID"
7. Select "Web application"
8. Add authorized redirect URIs:
   - `http://localhost:5000/api/auth/google/callback`
   - `http://localhost:3000`
9. Copy Client ID and Secret
10. Update `.env` file:
    ```
    GOOGLE_CLIENT_ID=your_client_id
    GOOGLE_CLIENT_SECRET=your_client_secret
    ```

## Verify Everything Works

### Backend Check
- Open http://localhost:5000/health
- Should show: `{"success": true, "message": "Server is running"}`

### Frontend Check
- Open http://localhost:3000
- Should show login page
- Try logging in with admin account

### Check MongoDB
```bash
# In mongo shell
mongo bmmusic
db.users.find()
db.songs.find()
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Cannot connect to MongoDB" | Ensure MongoDB service is running |
| "Address already in use" | Change PORT in .env or kill process on that port |
| "CORS Error" | Verify backend CORS config, check FRONTEND_URL |
| "Audio won't play" | Check browser console, verify files exist in database |
| "OTP not working" | Check browser console for the demo OTP |

## File Structure Quick Reference

```
SoundWave/
├── backend/
│   ├── server.js           ← Main server file
│   ├── seed.js             ← Sample data seeding
│   ├── .env                ← Configuration (create from .env.example)
│   ├── models/             ← Database schemas
│   ├── controllers/        ← Business logic
│   ├── routes/             ← API endpoints
│   └── middleware/         ← Auth, validation, errors
└── frontend/
    ├── index.html          ← Login page
    ├── dashboard.html      ← Main app
    ├── css/                ← Styling
    └── js/                 ← Frontend logic
```

## Next Steps

1. ✅ Backend running on port 5000
2. ✅ Frontend running on port 3000
3. ✅ Sample data loaded
4. ✅ Login with admin@bmmusic.com / password123
5. 🎵 Enjoy BM Music!

## Stopping Services

**Backend:**
```
Press Ctrl+C in backend terminal
```

**Frontend:**
```
Press Ctrl+C in frontend terminal
```

**MongoDB (if local):**
```bash
# Mac/Linux
brew services stop mongodb-community

# Windows
# Or just close the mongo server window
```

## Additional Commands

```bash
# Reset database
cd backend
node seed.js

# Install new packages
npm install package-name

# Check Node version
node --version

# Check npm version
npm --version
```

---

**For detailed information, see README.md in the main directory**
