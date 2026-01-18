from abc import abstractmethod, ABC


class Engine(ABC):
    def __init__(self, power):
        self.power = power

    @abstractmethod
    def start(self):
        pass