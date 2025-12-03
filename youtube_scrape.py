from youtube_transcript_api import YouTubeTranscriptApi
from pyyoutube import Client

f = open("YoutubeAPI.txt", "r")
API = f.read()
yt = YouTubeTranscriptApi()
client = Client(api_key=API)

playlist_id = "PL8DDJG7GRNac8Hf6NWtevdrGE1vkTL3oL"

video_ids = []
next_page = None

while True:
    resp = client.playlistItems.list(
        playlist_id=playlist_id,
        part="contentDetails",
        max_results=50,
        page_token=next_page
    )
    for item in resp.items:
        video_ids.append(item.contentDetails.videoId)
    next_page = resp.nextPageToken
    if not next_page:
        break

for i in video_ids:
    transcript = yt.fetch(i)
    f = open("youtube_transcripts/" + i + ".txt", "w")
    for snippet in transcript:
        f.write(snippet.text + "\n")
    f.close()


 


# video_id = "pqI5KPiTyjA"
# transcript = yt.fetch(video_id)

# f = open("youtube_transcripts/COSC 1010 Chapter 8 String methods.txt", "w")
# for snippet in transcript:
#     f.write(snippet.text + "\n")
# f.close()

