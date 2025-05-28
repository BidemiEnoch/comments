# Comments
A python library for pulling and applying sentiment analysis to youtube comments. It utilizes the Google client API to fetch Youtube data, and Huggingface transformers for machine learning tasks.

## Installation
```
git clone https://github.com/BidemiEnoch/comments.git
```
## Example usage
```python 
from comments import Client, analyze_sentiment, zero_shot_classification

key = "<Your Youtube API key>"
client = Client(key)

#Fetch 50 comments
comments = client.fetch_comments(content_id="<Youtube video ID>", sample_size = 50)

#You can perform sentiment analysis on the comments
sentiment = analyze_sentiment(comments)

#You can also perform classification tasks
classification = zero_shot_classification(
    comments, 
    labels = ["<Label 1>", "<Label 2>", "<Label 3>"]
    )
```
## Usage with specific models
```python
#You can specify a huggingface model for each task
sentiment = analyze_sentiment(
    comments, 
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )

classification = zero_shot_classification(
    comments, 
    labels = ["<Label 1>", "<Label 2>", "...","<Label n>"],
    model="facebook/bart-large-mnli"
    )
```
## About Huggingface models
Huggingface is a platform where the machine learning community collaborates on models, datasets, and applications. Read more https://huggingface.co/

## License
MIT







