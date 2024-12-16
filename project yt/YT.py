from googleapiclient.discovery import build
import isodate

API_KEY = 'AIzaSyAYV__-oyw8XxUDn2fasLNFOwjMdoCM0Dg'

def get_video_details(channel_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    video_request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    video_response = video_request.execute()

    if video_response.get("items"):
        video = video_response["items"][0]
        title = video["snippet"]["title"]
        publish_date = video["snippet"]["publishedAt"]
        thumbnail = video["snippet"]["thumbnails"]["high"]["url"]
        duration = isodate.parse_duration(video["contentDetails"]["duration"])
        likes = video["statistics"].get("likeCount", "N/A")
        channel_url = f"https://www.youtube.com/watch?v={channel_id}"

        print(f"Title: {title}")
        print(f"Publish Date: {publish_date}")
        print(f"Thumbnail: {thumbnail}")
        print(f"Duration: {str(duration)}")
        print(f"Likes: {likes}")
        print(f"Video URL: {channel_url}")
    else:
        print("Video not found")

channel_id = 'xpYu2gZ-FbE'
get_video_details(channel_id)