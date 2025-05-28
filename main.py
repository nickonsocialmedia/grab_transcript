# main.py
from youtube_transcript_api import YouTubeTranscriptApi
import os

def fetch_transcript(video_url):
    if "v=" not in video_url:
        print("Invalid URL.")
        return

    video_id = video_url.split("v=")[1].split("&")[0]
    print("Fetching transcript for video ID:", video_id)

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        print("\n--- Transcript ---\n")
        text = "\n".join(entry['text'] for entry in transcript)
        print(text)


        documents_path = os.path.expanduser("~/Documents")
        os.makedirs(documents_path, exist_ok=True)
        filename = os.path.join(documents_path, f"transcript_{video_id}.txt")

        with open(filename, "w") as f:
            f.write(text)

        print(f"\nTranscript saved to {filename}\n")

    except Exception as e:
        print(f"Error: {e}")

while True:
    url = input("Enter a YouTube video URL (or type 'q' to quit): ").strip()
    if url.lower() == 'q':
        print("Goodbye!")
        break
    fetch_transcript(url)
