from .step import Step
import os
from ..settings import COMPLETE_MASK_GEOTIFF, OUTPUT
from samgeo.common import raster_to_shp


class Geotiff2shp(Step):
    def process(self, data: dict, inputs: dict):
        raster_to_shp(COMPLETE_MASK_GEOTIFF, OUTPUT)

    def __str__(self):
        return "Geotiff2shp"
