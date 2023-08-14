from .step import Step
from samgeo.common import split_raster
from ...settings import SPLITED_TIFS_DIR
import os
import numpy as np


class CroppingTif(Step):
    def process(self, data: dict, inputs: dict):
        split_raster(inputs["source_tiffile"], SPLITED_TIFS_DIR, tile_size=inputs["tile_size"])

