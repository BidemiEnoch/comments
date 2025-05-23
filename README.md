# Comments
A python library for pulling and applying sentiment analysis to youtube comments.

## Quick start
```
git clone https://github.com/BidemiEnoch/comments.git
```
## Example usage
```python 
from comments import Client, analyze_sentiment

key = "<Your Youtube API key>"
client = Client(key)

results = analyze_sentiment(
    client=client,
    contentID="<Yotube video ID>",
    sampleSize=5
)
```
## License
MIT







