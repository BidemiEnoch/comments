from googleapiclient.discovery import build

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"


class Client:
    def __init__(self, api_key: str):
        self.reference = build(serviceName=API_SERVICE_NAME, version=API_VERSION, developerKey=api_key)

    def fetch_comments(self, *, content_id: str, sample_size: int = 100, trim_results: bool = True) -> dict:
        comments = []

        req = self.reference.commentThreads().list(part="snippet", videoId=content_id, maxResults=sample_size)
        res = req.execute()

        for index, item in enumerate(res["items"]):
            comment = item["snippet"]["topLevelComment"]["snippet"]
            if trim_results:
                comments.append({"seq": index, "textDisplay": comment["textDisplay"], "sentiment": []})
            else:
                comments.append(
                    {
                        "sequence": index,
                        "name": comment["authorDisplayName"],
                        "publishedAt": comment["publishedAt"],
                        "updatedAt": comment["updatedAt"],
                        "likeCount": comment["likeCount"],
                        "textDisplay": comment["textDisplay"],
                    }
                )

        return comments
