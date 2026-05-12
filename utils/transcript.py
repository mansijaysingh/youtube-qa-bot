from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url):

  pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"

  match= re.search(pattern, url)

  if match:
    return match.group(1)
  
  return None


def get_transcript(url):

  video_id= extract_video_id(url)

  ytt_api=YouTubeTranscriptApi()

  transcript=ytt_api.fetch(video_id)

  print(transcript)
  

if __name__ == "__main__":
  url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"

  get_transcript(url)