from .step import Step
from shpPredictor.Project_Nanshang.pipeline.settings import SPLITED_TIFS_DIR, MASK_DIR
import os
import numpy as np
import tifffile
from segment_anything import sam_model_registry, SamPredictor
import supervision as sv
from PIL import Image


class PredictMask(Step):

    def process(self, data: dict, inputs: dict):
        tifs_dir = os.listdir(SPLITED_TIFS_DIR)
        sam_predictor = self.load_segment_anything_model(inputs["sam_encoder_version"], inputs["sam_checkpoint_path"],
                                                         inputs["device"])
        mask_annotator = sv.MaskAnnotator()

        for tif in tifs_dir:
            # read tif as numpy array
            image = tifffile.imread(os.path.join(SPLITED_TIFS_DIR, tif))
            img_array = np.array(image)

            # make detection's mask
            data["detections"][tif].mask = self.segment(
                sam_predictor=sam_predictor,
                image=img_array.copy(),
                xyxy=data["detections"][tif].xyxy)

            # produce mask and save as image
            blank = np.zeros_like(img_array)
            mask = mask_annotator.annotate(scene=blank, detections=data["detection"][tif])
            img = Image.fromarray(mask, "RGB")
            img.save(os.path.join(MASK_DIR, "mask" + tif[4:-4] + ".jpg"))
        return data

    def segment(self, sam_predictor: "SamPredictor", image: np.ndarray, xyxy: np.ndarray) -> np.ndarray:
        sam_predictor.set_image(image)
        result_masks = []
        for box in xyxy:
            masks, scores, logits = sam_predictor.predict(
                box=box,
                multimask_output=True
            )
            index = np.argmax(scores)
            result_masks.append(masks[index])
        return np.array(result_masks)

    def load_segment_anything_model(self, sam_encoder_version, sam_checkpoint_path, device):
        sam = sam_model_registry[sam_encoder_version](checkpoint=sam_checkpoint_path).to(device=device)
        sam_predictor = SamPredictor(sam)
        return sam_predictor

    def __str__(self):
        return "PredictMask"