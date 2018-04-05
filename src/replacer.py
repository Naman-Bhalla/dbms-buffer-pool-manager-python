from abc import ABC, abstractmethod


class Replacer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def insert(self, frame):
        pass

    @abstractmethod
    def victim(self):
        pass

    @abstractmethod
    def erase(self, frame):
        pass

    @abstractmethod
    def __len__(self):
        pass
