from googleapiclient.discovery import build

api_service_name = "youtube"
api_version = "v3"


class Client:
    def __init__(self, api_key: str):
        self.reference = build(
            serviceName=api_service_name, version=api_version, developerKey=api_key
        )
        

    

