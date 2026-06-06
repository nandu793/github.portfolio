# Local Audio File Management Guide

## Overview

BM Music now uses **local audio files** stored in the `/songs` directory of your backend. This guide explains how to add, manage, and stream your own music files.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [File Organization](#file-organization)
3. [Supported Formats](#supported-formats)
4. [Metadata Extraction](#metadata-extraction)
5. [Seeding the Database](#seeding-the-database)
6. [API Endpoints](#api-endpoints)
7. [File Management](#file-management)
8. [Troubleshooting](#troubleshooting)
9. [Best Practices](#best-practices)

---

## Quick Start

### 1. Create Songs Directory
The `/songs` directory is automatically created when you run the seed script:
```bash
npm run dev
# The directory will be created at: backend/songs/
```

### 2. Add Audio Files
Copy your audio files to the `/songs` directory:
```
backend/
├── songs/
│   ├── Artist - Song Title.mp3
│   ├── Another Song.wav
│   └── Third Track.flac
├── server.js
└── ...
```

### 3. Seed the Database
Run the seed script to import songs:
```bash
cd backend
node seed.js
```

The script will:
- Detect all audio files in the `/songs` directory
- Extract metadata from filenames
- Create song entries in MongoDB
- Display import statistics

---

## File Organization

### Directory Structure
```
backend/
├── songs/                      # Audio files directory
│   ├── Track 1.mp3
│   ├── Track 2.wav
│   └── ...
├── utils/
│   └── audioFileManager.js     # File management utility
├── controllers/
│   └── songController.js       # Updated with local file streaming
├── routes/
│   └── songRoutes.js           # Updated with audio file endpoints
└── seed.js                     # Updated to read local files
```

### Creating the Songs Directory Manually
```bash
mkdir backend/songs
```

---

## Supported Formats

The following audio formats are supported:
- **MP3** (.mp3) - MPEG audio
- **WAV** (.wav) - Waveform audio
- **FLAC** (.flac) - Free Lossless Audio Codec
- **M4A** (.m4a) - MPEG-4 Audio
- **OGG** (.ogg) - Ogg Vorbis

### Quality Recommendations
- **Bitrate**: 128 kbps (streaming) to 320 kbps (high quality)
- **Sample Rate**: 44.1 kHz or 48 kHz
- **Channels**: Stereo (2 channels)
- **File Size**: Ideally under 50 MB per song

---

## Metadata Extraction

### Automatic Metadata from Filename

The system automatically extracts metadata from filenames:

#### Format 1: "Artist - Title"
```
Artist Name - Song Title.mp3
↓
Title: Song Title
Artist: Artist Name
Album: Local Music
```

#### Format 2: "Artist_Title"
```
Artist_Name_Song_Title.mp3
↓
Title: Song_Title
Artist: Artist_Name
Album: Local Music
```

#### Format 3: Title Only
```
Just A Song Title.mp3
↓
Title: Just A Song Title
Artist: Unknown Artist
Album: Local Music
```

### Manual Metadata Override
If automatic extraction doesn't work well, edit the seed.js to manually specify metadata:
```javascript
const customMetadata = {
  filename: 'audio.mp3',
  title: 'Custom Title',
  artist: 'Custom Artist',
  album: 'Custom Album',
  genre: 'Electronic',
  duration: 240 // seconds
};

const metadata = audioFileManager.getFileMetadata(
  customMetadata.filename,
  customMetadata
);
```

---

## Seeding the Database

### Default Workflow
```bash
cd backend
npm install
node seed.js
```

### What the Script Does
1. **Initializes songs directory** - Creates `/songs` folder if it doesn't exist
2. **Scans audio files** - Finds all supported audio files
3. **Extracts metadata** - Reads title, artist from filenames and file properties
4. **Creates song records** - Stores metadata in MongoDB
5. **Sets up admin user** - Creates test account (admin@bmmusic.com / password123)
6. **Creates playlists** - Sets up sample playlists with songs
7. **Displays statistics** - Shows import summary and file information

### Example Output
```
🗑️  Cleared existing data
✅ Admin user created

📁 Found 3 audio file(s) in /songs directory:
   Creating song entries from local audio files...

✅ 3 songs added to database

📊 Songs created:
   1. Midnight Dreams - The Echoes (245s, 8.50MB)
   2. Electric Pulse - Neon Vibes (198s, 6.75MB)
   3. Ocean Waves - Coastal Dreams (287s, 9.20MB)

✅ 2 sample playlists created

📈 Audio Files Statistics:
   Total files: 3
   Total size: 0.02 GB
   Total duration: 10 minutes

🎵 Database seeding completed successfully!
```

### Fallback to Defaults
If no audio files are found in `/songs`:
- The script creates sample song records using default metadata
- These are placeholder entries for development
- Add real audio files and re-run to replace them

---

## API Endpoints

### Get All Songs
```http
GET /api/songs
```
Return all songs stored in the database (from local files).

**Response:**
```json
{
  "success": true,
  "count": 10,
  "songs": [
    {
      "_id": "507f1f77bcf86cd799439011",
      "title": "Midnight Dreams",
      "artist": "The Echoes",
      "album": "Night Tales",
      "duration": 245,
      "filePath": "/songs/midnight-dreams.mp3",
      "streams": 1250,
      ...
    }
  ]
}
```

### Get Trending Songs
```http
GET /api/songs/trending
```
Returns the 10 most streamed songs.

### Search Songs
```http
GET /api/songs/search?q=artist
```
Search by title, artist, or album name.

### Stream Audio File
```http
GET /api/songs/stream/:id
```
Streams the audio file for a specific song. Supports:
- **HTTP Range requests** for resumable streaming
- **Partial content delivery** (206 status code)
- **Automatic stream counter increment**

**Example:**
```javascript
// Frontend code to stream audio
const audio = new Audio();
audio.src = '/api/songs/stream/507f1f77bcf86cd799439011';
audio.play();
```

### Get Local Audio Files Info
```http
GET /api/songs/audio/local
```
Get metadata about all audio files in the `/songs` directory.

**Response:**
```json
{
  "success": true,
  "message": "Local audio files retrieved",
  "data": {
    "files": [
      {
        "filename": "midnight-dreams.mp3",
        "extension": ".mp3",
        "size": 8912384,
        "sizeGB": "0.0083",
        "sizeMB": "8.50"
      }
    ],
    "statistics": {
      "totalFiles": 3,
      "totalSize": 24693504,
      "totalSizeGB": "0.023",
      "totalDurationMinutes": 10,
      "supportedFormats": [".mp3", ".wav", ".flac", ".m4a", ".ogg"]
    },
    "songsDirectory": "C:\\path\\to\\backend\\songs"
  }
}
```

---

## File Management

### AudioFileManager Utility

The `backend/utils/audioFileManager.js` provides methods for managing local audio files:

#### Initialize Directory
```javascript
audioFileManager.initSongsDirectory();
```

#### Get All Audio Files
```javascript
const files = audioFileManager.getAllAudioFiles();
// Returns: [{ filename, path, size, ext }, ...]
```

#### Get File Metadata
```javascript
const metadata = audioFileManager.getFileMetadata('song.mp3');
// Returns: { filename, title, artist, album, duration, filePath, ... }
```

#### Validate File
```javascript
const validation = audioFileManager.validateFile('song.mp3');
if (!validation.isValid) {
  console.log(validation.errors);
}
```

#### Get Statistics
```javascript
const stats = audioFileManager.getStatistics();
// Returns: { totalFiles, totalSize, totalDuration, ... }
```

#### Extract Metadata from Filename
```javascript
const meta = audioFileManager.extractMetadataFromFilename('Artist - Title.mp3');
// Returns: { artist, title, album }
```

---

## Adding New Songs

### Method 1: Manual Addition (Recommended)

1. **Place file in `/songs` directory:**
   ```bash
   cp "new_song.mp3" "backend/songs/"
   ```

2. **Update database:**
   ```bash
   cd backend
   node seed.js
   ```

3. **Access in application:**
   The new song will appear in:
   - GET /api/songs
   - GET /api/songs/search

### Method 2: Custom Metadata

Edit `seed.js` to add songs with custom metadata:
```javascript
const customSongs = [
  {
    filename: 'custom-song.mp3',
    title: 'My Custom Song',
    artist: 'My Name',
    album: 'My Album',
    genre: 'Pop',
    duration: 240
  }
];

customSongs.forEach(song => {
  const metadata = audioFileManager.getFileMetadata(
    song.filename,
    song
  );
  // Create song in database...
});
```

---

## Troubleshooting

### "Audio file not found" Error

**Problem:** When streaming, you get "Audio file not found"

**Solutions:**
1. Verify file exists in `/songs` directory:
   ```bash
   ls -la backend/songs/
   ```

2. Check file path in database:
   ```javascript
   // In MongoDB
   db.songs.findOne({ title: "Song Title" })
   // Check the 'filePath' field
   ```

3. Ensure MongoDB path matches actual file:
   - Database stores: `/songs/filename.mp3`
   - File location: `backend/songs/filename.mp3`

### Metadata not extracting correctly

**Problem:** Song title, artist show as "Unknown"

**Solutions:**
1. Verify filename format:
   - ✅ Correct: `Artist Name - Song Title.mp3`
   - ❌ Wrong: `Artist Name Song Title.mp3`

2. Manually override in seed.js:
   ```javascript
   const metadata = audioFileManager.getFileMetadata(
     'filename.mp3',
     { title: 'Actual Title', artist: 'Actual Artist' }
   );
   ```

### Large files causing issues

**Problem:** Files > 100MB cause warnings or slowness

**Solutions:**
1. Reduce file size:
   ```bash
   ffmpeg -i input.mp3 -b:a 128k output.mp3
   ```

2. Use lower bitrate:
   - Original: 320 kbps
   - Streaming: 128 kbps
   - Saves ~60% space

### Duration calculation incorrect

**Problem:** Song duration shows wrong in database

**Solutions:**
1. Database estimates based on file size, actual reading requires audio parsing
2. Set duration manually:
   ```javascript
   const metadata = audioFileManager.getFileMetadata(
     'song.mp3',
     { duration: 245 } // seconds
   );
   ```

---

## Best Practices

### 1. Filename Conventions
```
✅ Good
Artist Name - Song Title.mp3
Album Artist - Album Title - Track 01.mp3
Singer_Name_Great_Song.mp3

❌ Bad
songfile1.mp3
track_1.mp3
unknown.mp3
```

### 2. File Organization
```
backend/songs/
├── Rock/
│   └── Rock Artist - Rock Song.mp3
├── Pop/
│   └── Pop Artist - Pop Song.mp3
└── Electronic/
    └── Electronic Artist - Electronic Song.mp3
```
> Note: Recursive directory search is not yet supported. Keep all files in the root `/songs` directory.

### 3. Performance
- **Bitrate**: Use 192-256 kbps for good quality
- **Count**: 100+ songs work fine, 1000+ may impact sorting
- **Size**: Keep total folder under 1 GB for best performance

### 4. File Management
```bash
# Check total size
du -h backend/songs/

# Find files by extension
find backend/songs -name "*.mp3"

# Remove duplicates
find backend/songs -type f | sort | uniq -d

# Organize by artist
for file in *.mp3; do
  artist="${file%% - *}"
  mkdir -p "$artist"
  mv "$file" "$artist/"
done
```

### 5. Database Maintenance
```bash
# Clear and reseed
cd backend
node seed.js

# Remove specific song
# In MongoDB
db.songs.deleteOne({ title: "Song Title" })

# Backup songs metadata
mongodump --uri="mongodb://localhost:27017/bmmusic" --out="./backup"
```

### 6. Audio Quality Settings

| Use Case | Bitrate | Sample Rate | Format |
|----------|---------|-------------|--------|
| Streaming | 128 kbps | 44.1 kHz | MP3 |
| Normal playback | 192 kbps | 44.1 kHz | MP3 |
| High quality | 320 kbps | 48 kHz | FLAC/WAV |
| Lossless archive | 100% | 44.1+ kHz | FLAC |

---

## File Size Examples

File sizes (approximate) for a 3-minute song:

| Format | Bitrate | File Size |
|--------|---------|-----------|
| MP3 | 128 kbps | 2.8 MB |
| MP3 | 192 kbps | 4.3 MB |
| MP3 | 320 kbps | 7.2 MB |
| FLAC | Lossless | 25 MB |
| WAV | Lossless | 30 MB |

---

## Summary

✅ **Local audio files** - All music stored in `/songs` directory  
✅ **Automatic metadata** - Extracted from filenames  
✅ **HTTP streaming** - Range request support for resumable playback  
✅ **Database storage** - Song metadata in MongoDB  
✅ **Easy management** - Simple add/remove/reseed workflow  
✅ **No external APIs** - Complete independence from music services  

**Get started:** Place audio files in `/songs` and run `node seed.js`

