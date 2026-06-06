# 🔌 BM Music API Documentation

Complete API endpoint reference for BM Music backend.

## Base URL
```
http://localhost:5000/api
```

## Headers
All authenticated endpoints require:
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

---

## 🔐 Authentication Endpoints

### Register with Email
```
POST /auth/register
```

**Body:**
```json
{
  "email": "user@example.com",
  "username": "username",
  "password": "password123",
  "confirmPassword": "password123"
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "User registered successfully",
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "_id": "507f1f77bcf86cd799439011",
    "email": "user@example.com",
    "username": "username",
    "authMethod": "email",
    "isVerified": true
  }
}
```

### Login with Email
```
POST /auth/login
```

**Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": { /* user object */ }
}
```

### Send OTP (Phone Login)
```
POST /auth/send-otp
```

**Body:**
```json
{
  "phone": "1234567890"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "OTP sent successfully",
  "otpForDemo": "123456"
}
```

### Verify OTP & Login
```
POST /auth/verify-otp
```

**Body:**
```json
{
  "phone": "1234567890",
  "otp": "123456",
  "username": "username"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": { /* user object */ }
}
```

### Google OAuth
```
GET /auth/google
```
Redirects to Google login page.

### Google OAuth Callback
```
GET /auth/google/callback
```
Automatically handled by Passport.

### Get Current User
```
GET /auth/me
```
**Headers:** Requires Authorization header

**Response (200):**
```json
{
  "success": true,
  "user": {
    "_id": "507f1f77bcf86cd799439011",
    "email": "user@example.com",
    "username": "username",
    "profilePicture": "https://...",
    "bio": "Music lover",
    "favorites": [/* song ids */],
    "playlists": [/* playlist ids */]
  }
}
```

### Update Profile
```
PUT /auth/profile
```
**Headers:** Requires Authorization header

**Body:**
```json
{
  "username": "newusername",
  "bio": "New bio",
  "profilePicture": "https://..."
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Profile updated",
  "user": { /* updated user */ }
}
```

---

## 🎵 Song Endpoints

### Get All Songs
```
GET /songs
```

**Query Parameters:**
- `skip` (optional): Pagination offset
- `limit` (optional): Items per page

**Response (200):**
```json
{
  "success": true,
  "count": 5,
  "songs": [
    {
      "_id": "507f1f77bcf86cd799439011",
      "title": "Midnight Dreams",
      "artist": "The Echoes",
      "album": "Night Tales",
      "genre": "Electronic",
      "duration": 245,
      "coverArt": "https://...",
      "streams": 1250
    }
  ]
}
```

### Get Trending Songs
```
GET /songs/trending
```

**Response (200):**
```json
{
  "success": true,
  "count": 10,
  "songs": [ /* top 10 trending songs */ ]
}
```

### Get Song Details
```
GET /songs/:id
```

**Response (200):**
```json
{
  "success": true,
  "song": {
    "_id": "507f1f77bcf86cd799439011",
    "title": "Midnight Dreams",
    "artist": "The Echoes",
    "duration": 245,
    "coverArt": "https://...",
    "lyrics": "In the silence of the night...",
    "lyricsWithTimestamp": [
      {
        "time": 0,
        "text": "In the silence of the night"
      }
    ]
  }
}
```

### Stream Audio File
```
GET /songs/stream/:id
```

**Response:** Audio stream (audio/mpeg)

Supports HTTP range requests for seeking.

### Search Songs
```
GET /songs/search?q=query
```

**Query Parameters:**
- `q` (required): Search query (title, artist, album)

**Response (200):**
```json
{
  "success": true,
  "count": 3,
  "songs": [ /* matching songs */ ]
}
```

### Add to Favorites
```
POST /songs/:songId/favorite
```
**Headers:** Requires Authorization header

**Response (200):**
```json
{
  "success": true,
  "message": "Added to favorites",
  "favorites": [ /* array of favorite song ids */ ]
}
```

### Remove from Favorites
```
DELETE /songs/:songId/favorite
```
**Headers:** Requires Authorization header

**Response (200):**
```json
{
  "success": true,
  "message": "Removed from favorites",
  "favorites": []
}
```

### Get User Favorites
```
GET /songs/user/favorites
```
**Headers:** Requires Authorization header

**Response (200):**
```json
{
  "success": true,
  "count": 5,
  "favorites": [ /* array of favorite songs */ ]
}
```

---

## 📋 Playlist Endpoints

### Create Playlist
```
POST /playlists
```
**Headers:** Requires Authorization header

**Body:**
```json
{
  "name": "My Playlist",
  "description": "My favorite songs",
  "isPublic": true
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Playlist created",
  "playlist": {
    "_id": "507f1f77bcf86cd799439012",
    "name": "My Playlist",
    "owner": "507f1f77bcf86cd799439011",
    "songs": [],
    "isPublic": true
  }
}
```

### Get User Playlists
```
GET /playlists/user/my-playlists
```
**Headers:** Requires Authorization header

**Response (200):**
```json
{
  "success": true,
  "count": 3,
  "playlists": [ /* user's playlists */ ]
}
```

### Get Playlist Details
```
GET /playlists/:id
```

**Response (200):**
```json
{
  "success": true,
  "playlist": {
    "_id": "507f1f77bcf86cd799439012",
    "name": "My Playlist",
    "description": "My favorite songs",
    "owner": {
      "_id": "507f1f77bcf86cd799439011",
      "username": "username"
    },
    "songs": [ /* array of song objects */ ],
    "isPublic": true
  }
}
```

### Add Song to Playlist
```
POST /playlists/:id/add-song
```
**Headers:** Requires Authorization header

**Body:**
```json
{
  "songId": "507f1f77bcf86cd799439010"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Song added to playlist",
  "playlist": { /* updated playlist */ }
}
```

### Remove Song from Playlist
```
DELETE /playlists/:id/remove-song
```
**Headers:** Requires Authorization header

**Body:**
```json
{
  "songId": "507f1f77bcf86cd799439010"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Song removed from playlist",
  "playlist": { /* updated playlist */ }
}
```

### Delete Playlist
```
DELETE /playlists/:id
```
**Headers:** Requires Authorization header

**Response (200):**
```json
{
  "success": true,
  "message": "Playlist deleted"
}
```

### Get Public Playlists
```
GET /playlists/public
```

**Response (200):**
```json
{
  "success": true,
  "count": 10,
  "playlists": [ /* 20 public playlists */ ]
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "success": false,
  "message": "Invalid input",
  "status": 400
}
```

### 401 Unauthorized
```json
{
  "success": false,
  "message": "Token expired",
  "status": 401
}
```

### 403 Forbidden
```json
{
  "success": false,
  "message": "Not authorized to modify this playlist",
  "status": 403
}
```

### 404 Not Found
```json
{
  "success": false,
  "message": "Song not found",
  "status": 404
}
```

### 500 Server Error
```json
{
  "success": false,
  "message": "Server error",
  "status": 500
}
```

---

## Authentication

### JWT Token
Tokens are valid for 7 days.

**Token Structure:**
```
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUwN2YxZjc3YmNmODZjZDc5OTQzOTAxMSIsImlhdCI6MTY5NDQ4MjQ3MCwiZXhwIjoxNzAwNzM1MDcwfQ.abc123
```

### Using Token in Requests
```bash
curl -H "Authorization: Bearer YOUR_TOKEN_HERE" \
     http://localhost:5000/api/auth/me
```

---

## Code Examples

### JavaScript Fetch
```javascript
// Get trending songs
const response = await fetch('http://localhost:5000/api/songs/trending');
const data = await response.json();
console.log(data.songs);

// Login
const loginResponse = await fetch('http://localhost:5000/api/auth/login', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'password123'
  })
});
const loginData = await loginResponse.json();
const token = loginData.token;

// Get user with token
const userResponse = await fetch('http://localhost:5000/api/auth/me', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
const userData = await userResponse.json();
console.log(userData.user);
```

### Curl
```bash
# Get all songs
curl http://localhost:5000/api/songs

# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@bmmusic.com","password":"password123"}'

# Get trending songs
curl http://localhost:5000/api/songs/trending

# Stream song
curl http://localhost:5000/api/songs/stream/507f1f77bcf86cd799439011 \
  --output song.mp3
```

---

## Testing

**Test the API using:**
- Postman
- Insomnia
- Thunder Client (VS Code)
- cURL commands

---

## Rate Limiting
Currently no rate limiting. Consider adding for production.

## CORS
- Frontend: http://localhost:3000
- Add more origins in production

---

## Database Models

### User
```javascript
{
  _id: ObjectId,
  username: String,
  email: String,
  phone: String,
  password: String (hashed),
  googleId: String,
  profilePicture: String,
  bio: String,
  authMethod: String ('email', 'phone', 'google'),
  isVerified: Boolean,
  favorites: [ObjectId],
  playlists: [ObjectId],
  createdAt: Date,
  updatedAt: Date
}
```

### Song
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
  lyricsWithTimestamp: [{time: Number, text: String}],
  streams: Number,
  uploadedBy: ObjectId,
  createdAt: Date
}
```

### Playlist
```javascript
{
  _id: ObjectId,
  name: String,
  description: String,
  owner: ObjectId,
  songs: [ObjectId],
  coverImage: String,
  isPublic: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

---

For frontend code examples, see the JavaScript files in the `frontend/js/` directory.
