from transformers import pipeline

from .client import Client

api_service_name = "youtube"
api_version = "v3"


def analyze_sentiment(
    *, client: Client, contentID: str, sampleSize: int = 100, **kwargs
):
    comments = []
    analysis = []

    req = client.reference.commentThreads().list(
        part="snippet", videoId=contentID, maxResults=sampleSize
    )
    res = req.execute()

    for item in res["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]
        comments.append(
            {
                "name": comment["authorDisplayName"],
                "publishedAt": comment["publishedAt"],
                "updatedAt": comment["updatedAt"],
                "likeCount": comment["likeCount"],
                "textDisplay": comment["textDisplay"],
                "sentiment":[]
            }
        )

    if "model" in kwargs:
        transformer = pipeline("sentiment-analysis", model=kwargs["model"])
    else:
        transformer = pipeline("sentiment-analysis")

    analysis = transformer([comment["textDisplay"] for comment in comments])

    for i, result in enumerate(analysis):
            comments[i]["sentiment"] = result

    return comments
