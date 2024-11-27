from app.services.storage.aws_service import AWSStorage
from app.services.storage.azure_service import AzureStorage

# Factory Design Pattern

class StorageFactory:
    @staticmethod
    def get_cloud_provider(cloud_provider):
        if cloud_provider == "AWS":
            return AWSStorage()
        elif cloud_provider == "Azure":
            return AzureStorage()
        else:
            raise ValueError("Unsupported provider")