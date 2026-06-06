# SoundWave

A full-stack music streaming application built with Node.js, Express, MongoDB, JWT authentication, and a responsive HTML/CSS/JavaScript frontend.

## Features

- Email/password signup and login
- Phone login via OTP
- Google OAuth login
- JWT-protected backend routes
- Local audio streaming with HTTP Range support
- Music player controls, shuffle, repeat, and progress tracking
- Dual mode audio / lyrics player with timestamp synchronization
- Search, favorites, playlists, and responsive dashboard

## Quick Start

1. Install dependencies:
   ```bash
   npm install
   ```
2. Start MongoDB locally.
3. Configure `backend/.env` or copy `backend/.env.example`.
4. Start the app:
   ```bash
   npm start
   ```
5. Open `http://localhost:5000` in your browser.

## Folder Structure

```
SoundWave/
├── backend/
│   ├── server.js
│   ├── package.json
│   ├── .env
│   ├── .env.example
│   ├── config/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── songs/
│   ├── lyrics/
│   └── uploads/
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── css/style.css
│   ├── js/app.js
│   ├── js/auth.js
│   ├── js/player.js
│   ├── js/lyrics.js
│   ├── assets/images/
│   ├── assets/icons/
│   └── components/
│       ├── navbar.html
│       └── sidebar.html
├── .gitignore
└── README.md
```
