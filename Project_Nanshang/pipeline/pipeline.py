from typing import List
from .steps.step import StepException


class Pipeline:
    def __init__(self, steps: list):
        self.steps = steps

    def pipeline(self, inputs: dict):
        data = {}

        for step in self.steps:
            print(f"I'm now in {step}")
            try:
                data = step.process(data=data, inputs=inputs)
            except StepException as e:
                print(e, "happened in", step)
                break
