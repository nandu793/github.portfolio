# 🎵 BM Music - Quick Start Guide

Get BM Music running in 5 minutes!

## Prerequisites Checklist
- [ ] Node.js installed (https://nodejs.org)
- [ ] MongoDB installed or online (MongoDB Atlas)
- [ ] Two terminal windows open
- [ ] Browser ready

## Quick Start (5 Minutes)

### Using Local Audio Files (IMPORTANT!)

1. **Place audio files in the `/songs` directory:**
   ```bash
   # Copy your music files to:
   # SoundWave/backend/songs/
   
   # Supported formats: MP3, WAV, FLAC, M4A, OGG
   # Recommended filename format: "Artist - Song Title.mp3"
   
   Example:
   backend/songs/
   ├── The Beatles - Let It Be.mp3
   ├── Pink Floyd - Comfortably Numb.wav
   └── David Bowie - Heroes.flac
   ```

2. **Or use sample data (without audio files):**
   - Run the seed script without adding files
   - Default songs will be created for demonstration
   - No actual audio files needed for testing UI

### Terminal 1: Backend Setup

```bash
# 1. Navigate to backend
cd SoundWave/backend

# 2. Install dependencies (takes 1-2 min)
npm install

# 3. Add your music files to ./songs/ (optional)
# Create the songs directory if it doesn't exist:
mkdir songs
# Copy your audio files here

# 4. Seed database with songs from ./songs directory
node seed.js

# 5. Start backend server
npm start
```

**You should see:** `🎵 BM Music Backend Server running on port 5000`

The seed script will:
- ✅ Automatically create the `/songs` directory
- ✅ Scan for audio files (MP3, WAV, FLAC, M4A, OGG)
- ✅ Extract metadata from filenames
- ✅ Store song data in MongoDB
- ✅ Create sample playlists
- ✅ Display import statistics

### Terminal 2: Frontend Setup

```bash
# 1. Navigate to frontend (in new terminal)
cd SoundWave/frontend

# 2. Start web server (choose one)

# Using Python 3:
python -m http.server 3000

# OR Using Python 2:
python -m SimpleHTTPServer 3000

# OR Using Node.js:
npx http-server -p 3000
```

**You should see:** Server started at `http://localhost:3000`

### Browser

1. Open: http://localhost:3000
2. Click **Login** tab
3. Enter credentials:
   - **Email:** admin@bmmusic.com
   - **Password:** password123
4. Click **Login**
5. 🎉 **Enjoy Music Streaming!**

## Features to Try

### 1. **Music Player**
- Click any song to play
- Use Play/Pause, Previous, Next buttons
- Adjust volume with slider
- Seek using progress bar

### 2. **Lyrical Mode (Unique Feature!)**
- Click "📝 Lyrical Mode" button
- See synchronized lyrics
- Lyrics highlight as song plays
- Click lyrics to jump to that moment

### 3. **Create Playlist**
- Go to "Playlists" section
- Click "+ New Playlist"
- Add name and description
- Create!

### 4. **Add to Favorites**
- Click ♡ Favorite button while playing
- View favorites in "Library" section

### 5. **Search**
- Use search bar at top
- Find songs by title, artist, or album

## Troubleshooting

### Backend Won't Start
```
Error: Cannot connect to MongoDB
→ Solution: Start MongoDB service or check connection string in .env
```

### Port Already in Use
```
Error: listen EADDRINUSE: address already in use :::5000
→ Solution: Change PORT in backend/.env to 5001
```

### CORS Error
```
Error: Cross-Origin Request Blocked
→ Solution: Ensure backend is running on http://localhost:5000
```

### Audio Won't Play
```
Error: Audio file not found
→ Solution: Database might not be seeded - run: node seed.js
```

## Project Directory
```
SoundWave/
├── backend/           ← Node.js server
│   ├── .env          ← Configuration
│   ├── server.js     ← Start here
│   └── seed.js       ← Load sample data
└── frontend/         ← Web interface
    ├── index.html    ← Login page
    └── dashboard.html ← Main app
```

## Key Files to Know

| File | Purpose |
|------|---------|
| `backend/.env` | Configuration (port, database, etc) |
| `backend/seed.js` | Creates sample songs & user account |
| `backend/server.js` | Starts the API server |
| `frontend/index.html` | Login/Register page |
| `frontend/dashboard.html` | Main music app |

## Sample Account
- **Email:** admin@bmmusic.com
- **Password:** password123

Created by: `node seed.js`

## What's Included

✅ Email/Password Authentication  
✅ Phone OTP Login (Demo)  
✅ Google OAuth Ready  
✅ Music Streaming  
✅ **Lyrical Audio Mode** (Unique Feature!)  
✅ Playlists  
✅ Favorites  
✅ Search  
✅ Beautiful Dark UI  
✅ Responsive Design  

## Next Steps

1. ✅ Backend running
2. ✅ Frontend running
3. ✅ Logged in with sample account
4. 📚 Read README.md for detailed info
5. 🔐 Setup Google OAuth (optional)
6. 🚀 Customize and deploy!

## Stopping Services

```bash
# Backend: Press Ctrl+C in backend terminal
# Frontend: Press Ctrl+C in frontend terminal
```

## Common Commands

```bash
# Reset database
cd backend && node seed.js

# Check services running
# Backend: http://localhost:5000/health
# Frontend: http://localhost:3000

# View database
mongo bmmusic
> db.songs.find()
```

## Still Having Issues?

1. Check browser console for errors (F12)
2. Check terminal output for error messages
3. Verify MongoDB is running
4. Verify both servers are on correct ports
5. Try restarting services

## Ready to Code?

- **Backend:** Edit files in `backend/controllers/` and `backend/routes/`
- **Frontend:** Edit files in `frontend/js/` and `frontend/css/`
- **HotReload:** Backend with `npm run dev` (needs nodemon)

---

## Detailed Guides

For more detailed information:
- See **README.md** for full documentation
- See **SETUP.md** for detailed setup instructions
- Check **backend/seed.js** to understand data structure
- Explore **API endpoints** in README.md

---

**🎵 Happy Streaming!**

Questions? Errors? The app has everything needed - just follow the steps above!
