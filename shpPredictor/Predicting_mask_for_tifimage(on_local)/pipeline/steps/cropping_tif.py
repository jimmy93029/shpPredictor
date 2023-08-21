from .step import Step
from samgeo.common import split_raster
from shpPredictor.Project_Nanshang.pipeline.settings import SPLITED_TIFS_DIR


class CroppingTif(Step):
    def process(self, data: dict, inputs: dict):
        split_raster(inputs["source_tiffile"], SPLITED_TIFS_DIR, tile_size=inputs["tile_size"])
        return data

    def __str__(self):
        return "CroppingTif"

