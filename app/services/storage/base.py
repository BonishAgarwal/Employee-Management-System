from abc import ABC, abstractmethod

class StorageService(ABC):
    
    @abstractmethod
    def upload(self):
        pass
