from azure.storage.blob import BlobServiceClient
import json, yaml
import os

class BlobReader:
    def __init__(self, connection_string):
        self.client = BlobServiceClient.from_connection_string(connection_string)

    def read_blob(self, container_name, blob_name):
        blob_client = self.client.get_blob_client(container=container_name, blob=blob_name)
        content = blob_client.download_blob().readall()
        if blob_name.endswith(".json"):
            return json.loads(content)
        elif blob_name.endswith((".yml", ".yaml")):
            return yaml.safe_load(content)
        else:
            return content
