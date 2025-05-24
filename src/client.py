from googleapiclient.discovery import build
import pandas as pd

api_service_name = "youtube"
api_version = "v3"


class Client:
    def __init__(self, api_key: str, saveHistory: bool = True):
        self.reference = build(serviceName=api_service_name, version=api_version, developerKey=api_key)
        self.saveHistory = saveHistory
        self.history = []

    def DataFrame(self, *args):
        if len(args) > 0:
            return pd.DataFrame(args[0])
        else:
            return [pd.DataFrame(data) for data in self.history]
