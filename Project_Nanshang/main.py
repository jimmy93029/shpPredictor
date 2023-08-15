from .pipeline.pipeline import Pipeline
from .pipeline.steps.initialize_directory import InitializeDir
from .pipeline.steps.cropping_tif import CroppingTif
from .pipeline.steps.predict_bounding_box import PredictBoundingBox
from .pipeline.steps.predict_mask import PredictMask
from .pipeline.steps.merge_mask import MergeMask
from .pipeline.steps.image_to_geotiff import Image2Geotiff
from .pipeline.steps.geotiff_to_shp import Geotiff2shp
import torch


def main():
    inputs = {
        "model_arch": 'yolo_nas_l',
        "num_classes": 2,
        "checkpoint_path": None,
        "device": 'cuda' if torch.cuda.is_available() else "cpu",
        "confidence_threshold": 0.35,
        "sam_encoder_version": "vit_h",
        "source_tiffile": None,
        "tile_size": 700,
        "top_left_lat": 22.97494,
        "top_left_lon": 120.19544,
        "below_right_lat": 22.96717,
        "below_right_lon": 120.19775,

    }

    steps = [InitializeDir,
             CroppingTif,
             PredictBoundingBox,
             PredictMask,
             MergeMask,
             Image2Geotiff,
             Geotiff2shp
             ]

    p = Pipeline(steps)
    p.pipeline(inputs)


if __name__ == "__main__":
    main()
