from abc import ABC
from abc import abstractmethod


class Step(ABC):

    @abstractmethod
    def process(self, data: dict, inputs: dict):
        pass


class StepException(Exception):
    pass
