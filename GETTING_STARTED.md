# 🎵 BM Music - Getting Started Guide

Welcome to **BM Music** - A Full-Stack Music Streaming Application!

---

## 📋 Table of Contents

1. [File Structure](#file-structure)
2. [What Was Created](#what-was-created)
3. [Getting Started](#getting-started)
4. [Key Files to Know](#key-files-to-know)
5. [Next Steps](#next-steps)

---

## 📁 File Structure

```
SoundWave/
│
├── 📁 backend/
│   │
│   ├── 📁 config/
│   │   ├── 📄 db.js                    ← MongoDB connection
│   │   └── 📄 passport.js              ← OAuth strategy
│   │
│   ├── 📁 controllers/
│   │   ├── 📄 authController.js        ← Login/Register logic
│   │   ├── 📄 songController.js        ← Song management
│   │   └── 📄 playlistController.js    ← Playlist management
│   │
│   ├── 📁 middleware/
│   │   ├── 📄 auth.js                  ← JWT verification
│   │   ├── 📄 errorHandler.js          ← Error handling
│   │   └── 📄 inputValidator.js        ← Input validation
│   │
│   ├── 📁 models/
│   │   ├── 📄 User.js                  ← User schema
│   │   ├── 📄 Song.js                  ← Song schema
│   │   └── 📄 Playlist.js              ← Playlist schema
│   │
│   ├── 📁 routes/
│   │   ├── 📄 authRoutes.js            ← /api/auth endpoints
│   │   ├── 📄 songRoutes.js            ← /api/songs endpoints
│   │   └── 📄 playlistRoutes.js        ← /api/playlists endpoints
│   │
│   ├── 📁 uploads/                     ← Audio files folder (for future use)
│   │
│   ├── 📄 server.js                    ← 🚀 Main server file
│   ├── 📄 seed.js                      ← Database seeding script
│   ├── 📄 package.json                 ← Dependencies
│   ├── 📄 .env                         ← Configuration (created)
│   └── 📄 .env.example                 ← Configuration template
│
├── 📁 frontend/
│   │
│   ├── 📄 index.html                   ← 🔐 Login/Register page
│   ├── 📄 dashboard.html               ← 🎵 Main music app
│   │
│   ├── 📁 css/
│   │   ├── 📄 styles.css               ← Auth page styling
│   │   └── 📄 dashboard.css            ← Main app styling
│   │
│   ├── 📁 js/
│   │   ├── 📄 auth.js                  ← Authentication logic
│   │   ├── 📄 dashboard.js             ← Dashboard & playlists
│   │   └── 📄 player.js                ← Music player & lyrics
│   │
│   └── 📁 assets/                      ← Images (ready for use)
│
├── 📄 README.md                        ← 📘 Full documentation
├── 📄 QUICK_START.md                   ← ⚡ 5-minute setup
├── 📄 SETUP.md                         ← 🔧 Detailed setup
├── 📄 API_DOCUMENTATION.md             ← 🔌 API reference
├── 📄 ARCHITECTURE.md                  ← 🏗️ Technical design
├── 📄 SUMMARY.md                       ← 📊 Project summary
├── 📄 GETTING_STARTED.md               ← 📖 This file
├── 📄 .gitignore                       ← Git configuration
└── 📄 .env                             ← Configuration file

```

---

## ✅ What Was Created

### Backend (Node.js + Express)
| Component | Files | Purpose |
|-----------|-------|---------|
| **Server** | server.js | Express app initialization & routing |
| **Database** | config/db.js | MongoDB connection |
| **Authentication** | authController.js, authRoutes.js | Login, register, OAuth |
| **Music** | songController.js, songRoutes.js | Song streaming, search |
| **Playlists** | playlistController.js, playlistRoutes.js | Playlist management |
| **Security** | middleware/auth.js | JWT token verification |
| **Validation** | middleware/inputValidator.js | Input validation |
| **Errors** | middleware/errorHandler.js | Error handling |
| **Models** | models/*.js | Database schemas |
| **Seeding** | seed.js | Sample data creation |

### Frontend (HTML/CSS/JavaScript)
| Component | Files | Purpose |
|-----------|-------|---------|
| **Auth Pages** | index.html, auth.js | Login & registration UI |
| **Main App** | dashboard.html, dashboard.js | Music app interface |
| **Music Player** | dashboard.html, player.js | Audio playback & lyrics |
| **Styling** | css/*.css | Responsive design |

### Database (MongoDB)
| Collection | Fields | Purpose |
|-----------|--------|---------|
| **users** | email, password, favorites, playlists | User accounts |
| **songs** | title, artist, lyrics, duration | Music data |
| **playlists** | name, owner, songs | User playlists |

### Documentation
| File | Contents |
|------|----------|
| README.md | Complete feature guide |
| QUICK_START.md | 5-minute setup |
| SETUP.md | Detailed installation |
| API_DOCUMENTATION.md | API endpoints & examples |
| ARCHITECTURE.md | Technical design |
| SUMMARY.md | Project overview |

---

## 🚀 Getting Started

### Step 1: Backend Setup

```bash
# Navigate to backend
cd SoundWave/backend

# Install dependencies (one-time)
npm install

# Create sample database
node seed.js

# Start the server
npm start
```

**Output should show:**
```
✅ Admin user created
✅ 5 sample songs created
✅ Sample playlists created
🎵 BM Music Backend Server running on port 5000
```

### Step 2: Frontend Setup

Open a **new terminal**:

```bash
# Navigate to frontend
cd SoundWave/frontend

# Start web server (choose one)
python -m http.server 3000
```

**Output should show:**
```
Serving HTTP on 0.0.0.0 port 3000 (http://0.0.0.0:3000/) ...
```

### Step 3: Open Application

Open your browser:
```
http://localhost:3000
```

### Step 4: Login

**Admin Account:**
- Email: `admin@bmmusic.com`
- Password: `password123`

---

## 🔑 Key Files to Know

### 1️⃣ **Backend Server** (`backend/server.js`)
The main entry point that starts the Express server.
```javascript
// Starts on port 5000
// Mounts all routes
// Handles errors
```

### 2️⃣ **Database Connection** (`backend/config/db.js`)
Connects to MongoDB.
```javascript
// Uses MONGODB_URI from .env
// Handles connection errors
```

### 3️⃣ **Authentication** (`backend/controllers/authController.js`)
Handles user login, registration, and OAuth.
```javascript
// Email/password auth
// Phone OTP
// Google OAuth
```

### 4️⃣ **Music Player** (`frontend/js/player.js`)
Frontend music player logic.
```javascript
// Play, pause, next, previous
// Lyrics synchronization (unique feature!)
// Mode switcher
```

### 5️⃣ **Dashboard** (`frontend/dashboard.html`)
Main music streaming interface.
```html
<!-- Sidebar navigation -->
<!-- Music player -->
<!-- Lyrics panel (hidden by default) -->
```

### 6️⃣ **Configuration** (`backend/.env`)
Environment variables for the backend.
```
PORT=5000
MONGODB_URI=mongodb://localhost:27017/bmmusic
JWT_SECRET=your_secret_key
```

---

## 🎯 How Everything Works

### Authentication Flow
```
User enters credentials
         ↓
Frontend validates
         ↓
Backend verifies in MongoDB
         ↓
Password check (bcrypt)
         ↓
Generate JWT token
         ↓
Store token in localStorage
         ↓
Use token for protected routes
```

### Music Playback Flow
```
User clicks song
         ↓
Frontend loads song details (title, artist, lyrics)
         ↓
Get audio stream URL
         ↓
HTML5 audio player starts
         ↓
If Lyrical Mode: Display synchronized lyrics
         ↓
Song ends → Next song plays
```

### Unique Feature: Lyrical Mode
```
Traditional Player (Audio Only)
         ↓
Click "📝 Lyrical Mode" button
         ↓
Show synchronized lyrics
         ↓
Highlight current line as song plays
         ↓
User can click lyric to jump to that moment
         ↓
Switch back to Audio mode anytime
```

---

## 📊 Sample Data Included

### 5 Sample Songs
1. **Midnight Dreams** - The Echoes
2. **Electric Pulse** - Neon Vibes
3. **Ocean Waves** - Coastal Dreams
4. **Urban Jungle** - City Lights
5. **Sunset Symphony** - Golden Hour

Each song includes:
- ✅ Cover art
- ✅ Full metadata (artist, duration, genre)
- ✅ Complete lyrics
- ✅ Synchronized lyrics with timestamps
- ✅ Stream counter

### 2 Sample Playlists
- **Chill Vibes** - Relaxing songs
- **Energy Boost** - High energy tracks

### 1 Sample User
- Email: admin@soundwave.com
- Password: password123
- Includes: Favorites, playlists

---

## 🔌 API Structure

### Backend Routes
```
/api/auth/
  ├── POST /register        - Create account
  ├── POST /login          - Login
  ├── POST /send-otp       - Send OTP
  ├── POST /verify-otp     - Verify OTP
  ├── GET /google          - Google OAuth
  ├── GET /me              - Current user
  └── PUT /profile         - Update profile

/api/songs/
  ├── GET /                - All songs
  ├── GET /trending        - Top songs
  ├── GET /stream/:id      - Audio stream
  ├── GET /search?q=query  - Search
  ├── POST /:id/favorite   - Add favorite
  ├── DELETE /:id/favorite - Remove favorite
  └── GET /user/favorites  - User favorites

/api/playlists/
  ├── POST /               - Create
  ├── GET /user/my-playlists - User's playlists
  ├── GET /public          - Public playlists
  ├── GET /:id             - Details
  ├── POST /:id/add-song   - Add song
  ├── DELETE /:id/remove-song - Remove song
  └── DELETE /:id          - Delete playlist
```

### Frontend Pages
```
index.html
  ├── Login form
  ├── Registration form
  ├── Phone OTP form
  └── Google OAuth button

dashboard.html
  ├── Sidebar (navigation)
  ├── Top bar (search, user)
  ├── Content area (sections)
  │   ├── Home (trending)
  │   ├── Search
  │   ├── Library (favorites)
  │   ├── Playlists
  │   └── Profile
  └── Player section
      ├── Song info
      ├── Controls
      ├── Mode switcher
      └── Lyrics panel
```

---

## 🛠️ Common Tasks

### Add a New Song
1. Add to MongoDB using Compass
2. Include all fields: title, artist, lyrics, duration, etc.
3. Song appears immediately in app

### Customize Colors
1. Edit `frontend/css/dashboard.css`
2. Change `:root` CSS variables:
```css
:root {
  --primary-color: #1DB954;  /* Green */
  --secondary-color: #191414; /* Dark */
  /* etc */
}
```

### Change Database
1. Edit `backend/.env`
2. Update `MONGODB_URI`
3. Restart backend

### Test API
Use any API testing tool:
- Postman
- Insomnia
- Thunder Client
- cURL

```bash
curl http://localhost:5000/api/songs
```

---

## 🐛 If Something Breaks

### No backend response?
```bash
# Check if server is running
curl http://localhost:5000/health

# Check terminal for errors
# Restart: npm start
```

### Can't login?
```bash
# Reset database
node seed.js

# Try admin account
email: admin@soundwave.com
password: password123
```

### Audio won't play?
```bash
# Check browser console (F12)
# Verify songs in database
mongo bmmusic
db.songs.find()
```

### Port already in use?
```bash
# Change PORT in .env
PORT=5001

# Then restart
npm start
```

---

## 📚 Documentation Map

```
Need quick setup?
└─→ QUICK_START.md

Need detailed instructions?
└─→ SETUP.md

Need API reference?
└─→ API_DOCUMENTATION.md

Need technical details?
└─→ ARCHITECTURE.md

Need complete overview?
└─→ README.md

Need project summary?
└─→ SUMMARY.md

Lost? You're reading this!
└─→ GETTING_STARTED.md
```

---

## 🎯 What's Next?

### Immediate (5 minutes)
1. ✅ Start backend
2. ✅ Start frontend
3. ✅ Open browser to http://localhost:3000
4. ✅ Login with admin account
5. ✅ Explore the app!

### Short Term (30 minutes)
- Test all features
- Try lyrical mode
- Create a playlist
- Add favorites
- Search songs

### Medium Term (1-2 hours)
- Read full README.md
- Understand API structure
- Explore backend code
- Customize colors
- Add more sample songs

### Long Term (customization)
- Add your own songs
- Modify UI
- Add new features
- Deploy to production
- Implement Google OAuth

---

## 🎉 You're All Set!

Everything is set up and ready to run. The application includes:

✅ Complete backend with 20+ API endpoints
✅ Beautiful, responsive frontend
✅ Advanced music player with lyrics
✅ Multiple authentication methods
✅ Full playlist & favorites system
✅ Professional documentation

**Next step:** Run the commands in [Getting Started](#getting-started) section!

---

## 🤝 Need Help?

### Quick Issues
→ Check **QUICK_START.md** or **SETUP.md**

### API Questions
→ Check **API_DOCUMENTATION.md**

### Technical Questions
→ Check **ARCHITECTURE.md**

### Stuck?
1. Check browser console (F12)
2. Check terminal output
3. Verify MongoDB is running
4. Try restarting servers
5. Check documentation files

---

## 🎵 Happy Streaming!

Your **BM Music** music streaming application is complete and ready to use.

**Start coding!** 🚀
