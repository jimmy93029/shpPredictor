import os
import tifffile
import numpy as np
from .step import Step
from ..settings import SPLITED_TIFS_DIR
from super_gradients.training import models
import supervision as sv


class PredictBoundingBox(Step):

    def process(self, data: dict, inputs: dict):
        tifs_dir = os.listdir(SPLITED_TIFS_DIR)
        box_predictor = self.load_object_detection_model(inputs["model_arch"], inputs["num_classes"],
                                                 inputs["checkpoint_path"], inputs["device"])
        data["detections"] = {}

        num_tombs = 0
        for tif in tifs_dir:
            # read tif as numpy array
            image = tifffile.imread(os.path.join(SPLITED_TIFS_DIR, tif))
            img_array = np.array(image)

            # predict bounding box
            result = list(box_predictor.predict(img_array, conf=inputs["confidence_threshold"]))[0]
            boxes = result.prediction.bboxes_xyxy
            num_tombs += len(boxes)  # compute the number of tombs

            # make sv.Detections
            detection = sv.Detections(
                xyxy=boxes,
                confidence=result.prediction.confidence,
                class_id=result.prediction.labels.astype(int)
            )
            data["detections"][tif] = detection

        # finally we get the total number of tombs
        print(f"the number of tombs is {num_tombs}")
        data["num_tombs"] = num_tombs
        return data

    def load_object_detection_model(self, model_arch: str, num_classes: int, checkpoint_path: str, device: str):

        trained_model = models.get(
            model_arch,
            num_classes=num_classes,
            checkpoint_path=checkpoint_path
        ).to(device)

        return trained_model

    def __str__(self):
        return "PredictBoundingBox"