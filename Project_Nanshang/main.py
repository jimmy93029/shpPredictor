from .pipeline.pipeline import Pipeline
from .pipeline.steps.cropping_tif
from settings im

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