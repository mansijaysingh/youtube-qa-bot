from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url):

  pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"

  match= re.search(pattern, url)

  if match:
    return match.group(1)
  
  return None




def get_transcript(url):

  try:
     
     video_id=extract_video_id(url)

     if not video_id:
       return "Invalid YouTube URL"
     
     ytt_api=YouTubeTranscriptApi()

     transcript= ytt_api.fetch(video_id)

     full_text= " ".join(chunk.text for chunk in transcript)

     return full_text
  
  except Exception as e:

    error_message = str(e)

    if "No transcripts were found" in error_message:
        return "No transcript available for this video."

    elif "Transcripts are disabled" in error_message:
        return "Transcripts are disabled for this video."

    elif "Video unavailable" in error_message:
        return "This video is unavailable or private."

    else:
        return f"Error: {error_message}"






  