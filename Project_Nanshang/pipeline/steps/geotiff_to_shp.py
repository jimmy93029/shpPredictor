from .step import Step
import os
from ...settings import COMPLETE_MASK_GEOTIFF, OUTPUT_DIR
from samgeo.common import raster_to_shp


class Geotiff2shp(Step):
    def process(self, data: dict, inputs: dict):
        output_dir = self.make_output_dir(inputs["source_tiffile"])

        raster_to_shp(COMPLETE_MASK_GEOTIFF, output_dir)

    def make_output_dir(self, source_file):
        output_dir = OUTPUT_DIR
        if source_file.endswith('.tiff'):
            output_dir = os.path.join(OUTPUT_DIR, source_file[:-5])
        elif source_file.endswith('.tif'):
            output_dir = os.path.join(OUTPUT_DIR, source_file[:-5])
        os.makedirs(output_dir)
        return output_dir

