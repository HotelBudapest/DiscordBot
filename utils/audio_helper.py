import yt_dlp

def get_youtube_audio_url(url):
    """Extracts the audio stream URL from a YouTube video using yt-dlp."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': 'True',
        'extractaudio': True,
        'audioformat': 'mp3',
        'quiet': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info['url']
    except Exception as e:
        print(f"Error fetching audio from YouTube: {e}")
        return None
