import os
from .step import Step
from osgeo import gdal
from ...settings import MASK_DIR, COMPLETE_MASK_JPG
from PIL import Image


class MergeMask(Step):
    def process(self, data: dict, inputs: dict):
        height, width = self.read_tif(inputs["source_tiffile"])
        size = inputs["tile_size"]
        img = Image.new("RGB", (width, height))
        mask_dir = os.listdir(MASK_DIR)

        # collage small image to a complete image
        for mask_filename in mask_dir:
            im = Image.open(mask_filename)
            i = int(mask_filename[5])      # the 5th str indicate the order in x ray
            j = int(mask_filename[7])      # the 7th str indicate the order in y ray (see samgeo.common.split_raster())
            img.paste(im, (i * size, j * size))

        img.save(COMPLETE_MASK_JPG)
        return data

    def read_tif(self, tif_path):
        ds = gdal.Open(tif_path)
        row = ds.RasterXSize
        col = ds.RasterYSize
        return row, col



