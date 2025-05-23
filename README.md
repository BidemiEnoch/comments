# Comments
A python library for pulling and applying sentiment analysis with huggingface models to youtube comments.

## Quick start
```
git clone https://github.com/BidemiEnoch/comments.git
```
## Example usage
```python 
from comments import Client, analyze_sentiment

key = "<Your Youtube API key>"
client = Client(key)

analysis = analyze_sentiment(
    client,
    contentID="<Youtube video ID>",
    sampleSize=50
)

#You can also specify a model to be used for the analysis
analysis_with_model = analyze_sentiment(
    client,
    contentID="<Youtube video ID>",
    sampleSize=50,
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
)

#The client saves a history of every analysis
client.history

#You can get your results as a dataframe
dt = client.DataFrame(analysis_with_model)
#If no parameter is passed, it uses the saved client history
dt = client.DataFrame()
```
## License
MIT







