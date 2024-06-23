# YouTube MP3 Downloader 🎵

YouTube MP3 Bulk Downloader is a Python script that downloads audio streams from YouTube videos as MP3 files. It reads YouTube video URLs from a `youtube_urls.txt` file and downloads the audio using the `pytube` library.

## Features

- Downloads audio from YouTube videos as MP3 files.
- Utilizes `pytube` library for YouTube video handling.
- Simple and efficient batch download from a list of URLs.

## Requirements

- Python 3.x
- pytube library (`pip install pytube`)

## Usage

1. **Prepare `youtube_urls.txt` file:**
   - Create a text file named `youtube_urls.txt` in the same directory as the script.
   - Each line in `youtube_urls.txt` should contain a valid YouTube video URL.

2. **Run the script:**
   - Open a terminal or command prompt.
   - Ensure the `pytube` library is installed (`pip install pytube`) before running the script.
   - Navigate to the directory containing the script and `youtube_urls.txt`.
   - Run the script with Python:
     ```bash
     python3 ytmp3.py
     ```

3. **Wait for downloads:**
   - The script will iterate through each URL in `youtube_urls.txt`, download the audio as MP3, and save it in the current directory.


## Notes

- Ensure the `pytube` library is installed (`pip install pytube`) before running the script.
- Each URL in `youtube_urls.txt` should point to a YouTube video that allows extraction of audio streams.
- The downloaded MP3 files will be saved in the current directory.

