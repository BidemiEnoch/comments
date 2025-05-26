from transformers import pipeline
import pandas as pd


def analyze_sentiment(comments: dict, data_frame: bool = False, **kwargs) -> pd.DataFrame | dict:
    if "model" not in kwargs:
        kwargs["model"] = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    return __generic_task("sentiment-analysis", comments, data_frame, **kwargs)


def zero_shot_classification(comments: dict, labels: list, data_frame: bool = False, **kwargs) -> pd.DataFrame | dict:
    kwargs["labels"] = labels
    if "model" not in kwargs:
        kwargs["model"] = "facebook/bart-large-mnli"
    return __generic_task("zero-shot-classification", comments, data_frame, **kwargs)


def __generic_task(task: str, comments: dict, data_frame: bool, **kwargs) -> pd.DataFrame | dict:
    output = []
    pipe = pipeline(task, model=kwargs["model"])

    if task == "zero-shot-classification":
        analysis = pipe([comment["textDisplay"] for comment in comments], candidate_labels=kwargs["labels"])
    else:
        analysis = pipe([comment["textDisplay"] for comment in comments])

    for i, result in enumerate(analysis):
        output.append({"sequence_number": i, "taskOutput": result})

    return pd.DataFrame(output) if data_frame else output
