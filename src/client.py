from googleapiclient.discovery import build

api_service_name = "youtube"
api_version = "v3"


class Client:
    def __init__(self, api_key: str):
        self.reference = build(serviceName=api_service_name, version=api_version, developerKey=api_key)

    def fetch_comments(self, *, contentID: str, sampleSize: int = 100, trim_results: bool = True) -> dict:
        comments = []

        req = self.reference.commentThreads().list(part="snippet", videoId=contentID, maxResults=sampleSize)
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
