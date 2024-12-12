def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[-1]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")

import requests
from bs4 import BeautifulSoup

def scrape_title_and_date(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title
    title = soup.find("title").text.strip()

    # Extract upload date
    upload_date = soup.find("meta", itemprop="uploadDate")["content"]

    return title, upload_date

from youtube_transcript_api import YouTubeTranscriptApi

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = "\n".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        return "Transcript not available."

def get_youtube_data(url):
    # Extract video ID
    video_id = get_video_id(url)

    # Scrape title and upload date
    title, upload_date = scrape_title_and_date(url)

    # Fetch transcript
    transcript = fetch_transcript(video_id)

    return {
        "Title": title,
        "Upload Date": upload_date,
        "Transcript": transcript,
    }

youtube_url = "https://www.youtube.com/watch?v=Cgzakru7vms"
data = get_youtube_data(youtube_url)

print(f"Title: {data['Title']}")
print(f"Upload Date: {data['Upload Date']}")
print("Transcript:")
print(data['Transcript'])
