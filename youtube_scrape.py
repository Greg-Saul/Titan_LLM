from youtube_transcript_api import YouTubeTranscriptApi
import json

yt = YouTubeTranscriptApi()

video_id = "EWscNos-dFw"
transcript = yt.fetch(video_id)

f = open("transcript.txt", "w")
for snippet in transcript:
    f.write(snippet.text + "\n")
f.close()
