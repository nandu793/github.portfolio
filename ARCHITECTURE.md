# 🏗️ BM Music Architecture & Technical Design

Complete architectural overview of BM Music application.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Browser                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Frontend (HTML/CSS/JavaScript)          │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────┐  │   │
│  │  │   Login      │  │  Dashboard   │  │  Player  │  │   │
│  │  │   Register   │  │  Search      │  │  Lyrics  │  │   │
│  │  │   Auth       │  │  Playlists   │  │  Mode    │  │   │
│  │  └──────────────┘  └──────────────┘  └──────────┘  │   │
│  └────────────────────────────┬──────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                                │
                    HTTP/HTTPS (Fetch API)
                                │
┌─────────────────────────────────────────────────────────────┐
│                    Backend API (Node.js)                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                  Express.js Server                   │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────┐  │   │
│  │  │    Routes    │  │ Controllers  │  │ Middleware│  │   │
│  │  │  /auth       │  │ authCtrl     │  │   Auth   │  │   │
│  │  │  /songs      │  │ songCtrl     │  │  Errors  │  │   │
│  │  │  /playlists  │  │ playlistCtrl │  │Validator │  │   │
│  │  └──────────────┘  └──────────────┘  └──────────┘  │   │
│  └─────────────────┬──────────────────────────────────┘   │
│                    │                                        │
│  ┌──────────────────┴──────────────────────────────────┐   │
│  │            Modules & Utilities                      │   │
│  │  • JWT Token Generation & Verification             │   │
│  │  • Bcrypt Password Hashing                          │   │
│  │  • Passport.js OAuth Integration                    │   │
│  │  • Audio Streaming (Range Request Support)          │   │
│  │  • Input Validation                                 │   │
│  └──────────────────────────────────────────────────────┘   │
│                    │                                        │
└────────────────────┼────────────────────────────────────────┘
                     │
                  MongoDB
                     │
┌────────────────────┴────────────────────────────────────────┐
│                  MongoDB Database                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Collections:                                        │  │
│  │  • users       - User accounts & profiles           │  │
│  │  • songs       - Songs with lyrics & metadata        │  │
│  │  • playlists   - User-created playlists             │  │
│  │  • sessions    - User session data                   │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## Data Flow

### Authentication Flow

```
User Input (Email/Password/Phone/Google)
         │
         ▼
    Validation Middleware
         │
         ├─ Valid? 
         │  └─ No → Error Response (400)
         │
         └─ Yes
            │
            ▼
      Authentication Controller
         │
         ├─ Email/Password/Phone:
         │  ├─ Check if user exists
         │  ├─ Hash password
         │  └─ Save to MongoDB
         │
         └─ Google OAuth:
            ├─ Verify Google token
            ├─ Get user info from Google
            └─ Create/Update user in MongoDB
         │
         ▼
    Generate JWT Token
         │
         ▼
   Return Token + User Data
         │
         ▼
   Store in localStorage
         │
         ▼
   Use in all further requests
```

### Music Streaming Flow

```
User Clicks Song
         │
         ▼
Frontend Requests Song Details
         │
         ├─ GET /api/songs/:id
         │  └─ Returns title, artist, lyrics, etc.
         │
         ▼
Frontend Loads Audio Stream
         │
         ├─ GET /api/songs/stream/:id
         │  └─ Supports HTTP Range Requests
         │
         ▼
Audio Player Starts
         │
         ├─ Play/Pause/Volume/Seek
         │  └─ All handled client-side
         │
         └─ If Lyrical Mode enabled:
            ├─ Display synchronized lyrics
            ├─ Highlight current lyric
            └─ Jump to timestamp on click
         │
         ▼
Song Ends
         │
         └─ Increment stream counter in DB
```

### Playlist Management Flow

```
User Creates Playlist
         │
         ▼
POST /api/playlists
         │
         ├─ Auth Check (JWT)
         ├─ Validate input
         ├─ Create playlist in MongoDB
         └─ Link to user account
         │
         ▼
User Adds Song to Playlist
         │
         ├─ POST /api/playlists/:id/add-song
         ├─ Verify ownership
         ├─ Check duplicate
         ├─ Add song reference
         └─ Save to database
         │
         ▼
Playlist Updated in UI
         │
         └─ Refresh from database
```

---

## Module Breakdown

### Backend Structure

#### 1. **Routes** (`backend/routes/`)
Defines API endpoints:
- `authRoutes.js` - Login, register, OAuth flows
- `songRoutes.js` - Song search, streaming, favorites
- `playlistRoutes.js` - Playlist CRUD operations

#### 2. **Controllers** (`backend/controllers/`)
Business logic for each route:
- `authController.js` - User authentication logic
- `songController.js` - Song management logic
- `playlistController.js` - Playlist management logic

#### 3. **Models** (`backend/models/`)
MongoDB schemas:
- `User.js` - User document schema with methods
- `Song.js` - Song metadata and lyrics
- `Playlist.js` - Playlist structure

#### 4. **Middleware** (`backend/middleware/`)
Request processing functions:
- `auth.js` - JWT verification & token generation
- `errorHandler.js` - Centralized error handling
- `inputValidator.js` - Input validation rules

#### 5. **Configuration** (`backend/config/`)
- `db.js` - MongoDB connection
- `passport.js` - OAuth strategy setup

#### 6. **Main Server** (`backend/server.js`)
- Express app initialization
- Middleware setup
- Route mounting
- Error handling setup

### Frontend Structure

#### 1. **HTML** (`frontend/`)
- `index.html` - Authentication pages
- `dashboard.html` - Main application interface

#### 2. **CSS** (`frontend/css/`)
- `styles.css` - Auth page styling
- `dashboard.css` - Main app styling & responsive design

#### 3. **JavaScript** (`frontend/js/`)
- `auth.js` - Authentication logic (login, register, OAuth)
- `dashboard.js` - Dashboard, playlists, favorites
- `player.js` - Music player, mode switching, lyrics

---

## Key Features & Implementation

### 1. Authentication System

**Email/Password:**
- Input validation
- Bcrypt hashing (10 rounds)
- MongoDB storage
- JWT token generation (7-day expiry)

**Phone OTP:**
- Random 6-digit OTP generation
- 5-minute expiration
- Mock SMS integration (logs to console)
- Same registration flow

**Google OAuth:**
- Passport.js integration
- Google Strategy configuration
- Automatic user creation/update
- Secure redirect flow

### 2. Music Streaming

**HTTP Streaming:**
- Supports range requests for seeking
- Proper MIME type headers
- Stream counter increment

**Lyrics Synchronization:**
- Timestamp-based lyrics data
- Backend stores in database
- Frontend displays with playback sync
- Click-to-jump functionality

### 3. Audio Splitter (Unique Feature)

**Mode Switcher Implementation:**
```javascript
// Two modes available
"Audio Only" - Traditional player
"Lyrical Mode" - Synchronized lyrics display

// Backend provides:
lyricsWithTimestamp: [
  {time: 0, text: "First line"},
  {time: 5, text: "Second line"},
  ...
]

// Frontend handles:
1. Display lyrics
2. Sync with playback time
3. Highlight current lyric
4. Smooth scrolling
5. Click to jump
```

### 4. Favorites System

**Frontend:**
1. Heart button (♡/❤️) on player
2. Toggle favorite status
3. Visual feedback

**Backend:**
1. Add/remove from user.favorites array
2. GET endpoint to retrieve all
3. Validation for duplicates

### 5. Playlist Management

**Features:**
- Create with name and description
- Add/remove songs
- Public/private toggle
- Owner verification
- Browse public playlists

---

## Security Measures

### 1. Password Security
```javascript
// Bcrypt hashing (10 rounds)
const hashedPassword = await bcrypt.hash(password, 10);
// Verify on login
const isValid = await bcrypt.compare(inputPassword, hashedPassword);
```

### 2. JWT Authentication
```javascript
// Token structure
{
  id: userId,
  iat: issued_at,
  exp: expiration (7 days)
}

// Verification on protected routes
const decoded = jwt.verify(token, JWT_SECRET);
```

### 3. Input Validation
```javascript
// Email, phone, password validation
// Prevents injection attacks
// Sanitizes user input
```

### 4. CORS Protection
```javascript
app.use(cors({
  origin: process.env.FRONTEND_URL,
  credentials: true
}))
```

### 5. Error Handling
```javascript
// Centralized middleware
// Doesn't expose database details
// Handles JWT errors properly
```

---

## Database Schema

### Users Collection
```javascript
{
  _id: ObjectId,
  username: String,
  email: String (unique),
  phone: String (unique),
  password: String (hashed),
  googleId: String (unique),
  profilePicture: String,
  bio: String,
  authMethod: String,
  isVerified: Boolean,
  favorites: [SongId],
  playlists: [PlaylistId],
  createdAt: Date,
  updatedAt: Date
}
```

### Songs Collection
```javascript
{
  _id: ObjectId,
  title: String,
  artist: String,
  album: String,
  genre: String,
  duration: Number,
  filePath: String,
  coverArt: String,
  lyrics: String,
  lyricsWithTimestamp: [
    {time: Number, text: String}
  ],
  streams: Number,
  uploadedBy: UserId,
  createdAt: Date
}
```

### Playlists Collection
```javascript
{
  _id: ObjectId,
  name: String,
  description: String,
  owner: UserId,
  songs: [SongId],
  coverImage: String,
  isPublic: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

---

## API Request/Response Flow

### Example: Login Request
```javascript
// Frontend
fetch('http://localhost:5000/api/auth/login', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'password123'
  })
})

// Backend Processing
1. Route handler receives request
2. Validation middleware checks input
3. Controller finds user in DB
4. Compares password with bcrypt
5. If valid: generates JWT token
6. Returns token + user data

// Frontend receives
{
  success: true,
  token: "eyJ...",
  user: {...}
}

// Frontend stores
localStorage.setItem('token', token);
localStorage.setItem('user', JSON.stringify(user));

// Future requests
fetch(url, {
  headers: {
    'Authorization': `Bearer ${token}`
  }
})
```

---

## Performance Considerations

### 1. Audio Streaming
- HTTP Range Requests allow seeking without downloading full file
- Proper Content-Length headers
- Stream MIME type set to audio/mpeg

### 2. Database Queries
- Indexes on email, phone, googleId for fast lookups
- Population of references (user data in playlists)
- Pagination ready for large results

### 3. Frontend Optimization
- No unnecessary re-renders
- Event delegation for context menus
- Efficient DOM manipulation
- CSS Grid for responsive layouts

### 4. Caching
- User data cached in localStorage
- JWT tokens included in requests
- Frontend caches loaded data

---

## Scalability Notes

### Current (Development)
- Single server instance
- Local/Atlas MongoDB
- In-memory OTP store

### For Production Scale Up
- Load balancer for multiple server instances
- Redis cache for OTP and sessions
- Database replication & sharding
- CDN for audio files
- Queue system for heavy operations
- Monitoring & logging

---

## Development Workflow

### Adding New Feature

1. **Backend:**
   - Create route in `routes/`
   - Create controller logic in `controllers/`
   - Add/update model in `models/`
   - Test with Postman

2. **Frontend:**
   - Add HTML elements in `dashboard.html`
   - Add CSS in `css/dashboard.css`
   - Add event listeners in `js/dashboard.js` or `js/player.js`
   - Test in browser

3. **Testing:**
   - Test API endpoint with curl/Postman
   - Test frontend functionality
   - Check browser console for errors
   - Verify database changes

---

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| CORS Error | Frontend/Backend not matching | Check FRONTEND_URL in .env |
| Auth fails | Token invalid/expired | Clear localStorage, login again |
| Audio won't play | File not found or streaming error | Check database, verify seed |
| Lyrics not showing | Missing lyricsWithTimestamp | Verify song data in DB |

---

## Code Examples

### Adding a Song to Favorites (Backend)
```javascript
// In songController.js
const addToFavorites = async (req, res) => {
  const {songId} = req.params;
  const user = await User.findByIdAndUpdate(
    req.userId,
    {$addToSet: {favorites: songId}}, // addToSet prevents duplicates
    {new: true}
  ).populate('favorites');
  
  res.json({success: true, favorites: user.favorites});
};
```

### Displaying Lyrics (Frontend)
```javascript
// In player.js
function displayLyrics(lyricsData) {
  lyricsData.forEach(lyric => {
    const line = document.createElement('div');
    line.className = 'lyric-line';
    line.textContent = lyric.text;
    
    // Allow clicking to jump
    line.addEventListener('click', () => {
      audioPlayer.currentTime = lyric.time;
      audioPlayer.play();
    });
    
    lyricsContent.appendChild(line);
  });
}

// Update on playback
audioPlayer.addEventListener('timeupdate', () => {
  // Find current lyric and highlight
  currentSong.lyricsWithTimestamp.forEach(lyric => {
    if (audioPlayer.currentTime >= lyric.time) {
      // Highlight this lyric
    }
  });
});
```

---

## Deployment Checklist

- [ ] Environment variables configured
- [ ] Database security enabled
- [ ] HTTPS enabled
- [ ] CORS restricted to production domain
- [ ] Secrets changed (JWT, session keys)
- [ ] Rate limiting added
- [ ] Logging configured
- [ ] Monitoring set up
- [ ] Backups scheduled
- [ ] SSL certificates valid

---

This architecture is scalable, secure, and maintainable for a modern music streaming application.
