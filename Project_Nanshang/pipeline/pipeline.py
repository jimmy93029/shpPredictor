from typing import List
from .steps.step import StepException


class Pipeline:
    def __init__(self, steps: list):
        self.steps = steps

    def pipeline(self, inputs: dict):
        data = None

        for step in self.steps:
            try:
                data = step.process(data, inputs)
            except StepException as e:
                print(e, "happened in", step)
                break
