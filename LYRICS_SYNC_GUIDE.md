# 🎵 BM Music - Enhanced Lyrics Synchronization Guide

## Overview

The BM Music application now includes **advanced lyrical synchronization** with millisecond-precision timestamps, making lyrics display perfectly in sync with the audio playback.

## Key Features

### 1. **Precision Timestamp Format**
- **Old Format:** `{ time: 5, text: "Lyric text" }` (seconds only)
- **New Format:** `{ startTime: 5000, endTime: 10000, text: "Lyric text" }` (milliseconds with duration)

The new format provides:
- ✅ Millisecond-level precision
- ✅ Explicit duration for each lyric line
- ✅ Better handling of overlapping text
- ✅ Smoother transitions between lyrics

### 2. **Real-Time Synchronization**
The player continuously monitors playback position and:
- Highlights the currently active lyric line
- Auto-scrolls to keep the active lyric visible
- Smoothly transitions as you play through the song
- Works with both seeking and normal playback

### 3. **Enhanced Interactive Features**
- **Click-to-Sync:** Click any lyric to jump to that timestamp
- **Time Display:** Each lyric shows its start time in `mm:ss` format
- **Hover Effects:** Visual feedback when hovering over lyrics
- **Active Highlighting:** Current lyric is clearly highlighted

## JSON Format Specification

### Standard Lyric Object
```json
{
  "startTime": 5000,
  "endTime": 10000,
  "text": "Lyric text goes here"
}
```

**Field Descriptions:**
- `startTime` (number): When this lyric begins, in milliseconds
- `endTime` (number): When this lyric ends, in milliseconds
- `text` (string): The lyric content to display

### Complete Song Example
```json
{
  "title": "Song Title",
  "artist": "Artist Name",
  "duration": 245,
  "lyricsWithTimestamp": [
    {
      "startTime": 0,
      "endTime": 5500,
      "text": "First line of lyrics"
    },
    {
      "startTime": 5500,
      "endTime": 10000,
      "text": "Second line of lyrics"
    },
    {
      "startTime": 10000,
      "endTime": 15000,
      "text": "Third line of lyrics"
    }
  ]
}
```

## Using the LyricsSync Utility

The application includes a powerful `LyricsSync` class for managing lyrics programmatically.

### Basic Usage

```javascript
// Create instance
const sync = new LyricsSync();

// Load lyrics from JSON
const lyrics = [
  { startTime: 0, endTime: 5000, text: "Line 1" },
  { startTime: 5000, endTime: 10000, text: "Line 2" }
];
sync.currentLyrics = sync.normalizeLyrics(lyrics);

// Find current lyric
const currentTimeMs = audioPlayer.currentTime * 1000;
const { lyric, index } = sync.findCurrentLyric(currentTimeMs);
console.log(`Currently on lyric ${index}: ${lyric.text}`);

// Get statistics
const stats = sync.getStatistics();
console.log(`Total lyrics: ${stats.count}, Duration: ${stats.durationFormatted}`);
```

### Format Conversion

#### Import from JSON
```javascript
const jsonString = '[{"startTime": 0, "endTime": 5000, "text": "Line 1"}]';
sync.importFromJSON(jsonString);
```

#### Export to JSON
```javascript
const jsonOutput = sync.exportToJSON();
console.log(jsonOutput);
```

#### Parse LRC Format
```javascript
const lrcContent = `[00:00.00]First line
[00:05.00]Second line
[00:10.00]Third line`;

sync.parseLRC(lrcContent);
```

#### Export to LRC Format
```javascript
const lrcOutput = sync.exportToLRC();
// Output: [00:00.00]First line
//         [00:05.00]Second line
```

### Validation

```javascript
const validation = sync.validate(lyrics);
if (!validation.valid) {
  console.warn('Issues found:', validation.issues);
}
// Returns: { valid: true/false, issues: [...] }
```

### Timestamp Adjustment

```javascript
// Shift all lyrics by 500ms earlier
sync.adjustTimestamps(-500);

// Or 500ms later
sync.adjustTimestamps(500);
```

## Synchronization Algorithm

The player uses three-step synchronization:

### 1. **Time Comparison**
- Converts current playback time to milliseconds
- Compares against each lyric's `startTime` and `endTime`

### 2. **Active Lyric Detection**
```javascript
const currentTimeMs = audioPlayer.currentTime * 1000;
for (let i = 0; i < lyrics.length; i++) {
  const lyric = lyrics[i];
  if (currentTimeMs >= lyric.startTime && 
      currentTimeMs < lyric.endTime) {
    // This lyric is active
  }
}
```

### 3. **Smooth Highlighting & Scrolling**
- Removes previous active state
- Applies active class to current lyric
- Auto-scrolls to center active lyric in view

## Best Practices for Lyric Timing

### 1. **Consistent Time Intervals**
- Ensure `endTime` of one lyric equals `startTime` of next
- Avoid gaps or overlaps

```javascript
// ✅ Good
{ startTime: 0, endTime: 5000, text: "Line 1" }
{ startTime: 5000, endTime: 10000, text: "Line 2" }

// ❌ Avoid - gap
{ startTime: 0, endTime: 5000, text: "Line 1" }
{ startTime: 5500, endTime: 10500, text: "Line 2" }
```

### 2. **Realistic Line Duration**
- Base duration on how long the lyric should be read
- Typically 3-8 seconds per line for singing
- Shorter for rapid lyrics, longer for drawn-out notes

```javascript
// Short, rapid lyrics: ~2-3 seconds
{ startTime: 0, endTime: 2500, text: "Yeah" }

// Normal lyrics: ~4-5 seconds
{ startTime: 5000, endTime: 10000, text: "This is a normal line" }

// Long, sustained notes: ~6-8 seconds
{ startTime: 20000, endTime: 28000, text: "Sustained noooote" }
```

### 3. **Precision Timing**
- Use `mmm:ss.cs` format when available (minutes:seconds.centiseconds)
- For sub-second precision, use milliseconds
- Test synchronization at various playback speeds

## Backward Compatibility

The system automatically handles both old and new formats:

```javascript
// Old format (still supported)
{ time: 5, text: "Lyric" } → Converts to { startTime: 5000, endTime: 10000 }

// New format (recommended)
{ startTime: 5000, endTime: 10000, text: "Lyric" }
```

## Advanced Features

### Get Highlighted Lyrics
```javascript
const highlightedIndices = sync.getHighlightedLyrics(currentTimeMs);
// Returns array of lyric indices within sync tolerance
```

### Format Time Helper
```javascript
const formatted = sync.formatTime(65.5); // Returns "1:05.50"
```

### Statistics
```javascript
const stats = sync.getStatistics();
console.log(stats);
// Output:
// {
//   count: 48,
//   duration: 245000,
//   durationFormatted: "4:05.00",
//   avgDuration: 5104.17,
//   avgDurationFormatted: "0:05.10"
// }
```

## Debugging Lyrics

### Enable Logging
```javascript
// In player.js, add:
console.log('Current lyrics:', lyricsSync.currentLyrics);
console.log('Statistics:', lyricsSync.getStatistics());
```

### Validate Before Playing
```javascript
const validation = lyricsSync.validate(song.lyricsWithTimestamp);
console.log('Validation:', validation);
```

### Check Synchronization Quality
```javascript
const stats = lyricsSync.getStatistics();
if (stats.count > 0 && stats.duration < (song.duration * 1000 * 0.8)) {
  console.warn('Warning: Lyrics cover less than 80% of song duration');
}
```

## Performance Considerations

### Optimization Tips
1. **Lyric Count:** 50-100 lines is optimal for most songs
2. **Update Frequency:** Synchronization checks on `timeupdate` events
3. **Rendering:** Only active lyric is highlighted (efficient DOM manipulation)

### Memory Usage
- Small JSON payloads (typically < 2KB per song)
- Efficient array operations
- No external dependencies

## Troubleshooting

### Lyrics Not Syncing Properly
1. **Check Format:** Verify `startTime` and `endTime` exist
2. **Check Values:** Ensure times are in milliseconds, not seconds
3. **Validate:** Run `sync.validate()` to catch issues

### Lyrics Jumping Around
- **Cause:** Overlapping time ranges
- **Solution:** Ensure `endTime` of one = `startTime` of next

### Lyrics Not Displaying at All
- **Cause:** No `lyricsWithTimestamp` in song data
- **Solution:** Reseed database: `npm run seed`

### Scrolling Not Smooth
- **Cause:** Too many lyrics on screen
- **Solution:** Limit visible lyrics, use CSS overflow handling

## API Endpoints

### Get Song with Lyrics
```
GET /api/songs/:id
Response includes: lyricsWithTimestamp array
```

### Search Songs
```
GET /api/songs/search?q=query
Returns songs with lyrics data
```

## Sample Data

The database includes 5 sample songs with properly synchronized lyrics:

1. **Midnight Dreams** - 8 lyrics, 245 seconds
2. **Electric Pulse** - 8 lyrics, 198 seconds
3. **Ocean Waves** - 8 lyrics, 287 seconds
4. **Urban Jungle** - 8 lyrics, 213 seconds
5. **Sunset Symphony** - 8 lyrics, 264 seconds

Each lyric is precisely timed with millisecond accuracy.

## Future Enhancements

Planned features for lyrics synchronization:

- 🎯 **Auto-Sync:** Automatic detection from audio analysis
- 🎨 **Karaoke Mode:** Highlighted text color segments per syllable
- 📝 **Lyric Editor:** In-app editor for adjusting timestamps
- 🔄 **LRC Import:** Upload LRC files directly
- 🎤 **Vocal Detection:** Automatic silence-based sync
- 📊 **Batch Sync:** Process multiple songs at once

## Support & Documentation

For more information:
- See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for API details
- See [ARCHITECTURE.md](ARCHITECTURE.md) for system design
- See [README.md](README.md) for general setup

---

**Version:** 1.0  
**Last Updated:** February 2026  
**Format Version:** JSON with millisecond precision
