class Observer:
    def notify(self, data):
        raise NotImplementedError("Subclasses must implement 'notify'")

class Subject:
    def __init__(self):
        self._observers = []
    
    def add_observers(self, observer: Observer):
        self._observers.append(observer)
    
    def notify_observers(self, data):
        for observer in self._observers:
            observer.notify(data)
        