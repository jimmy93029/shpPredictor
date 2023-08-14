import os
import numpy as np
from .step import Step
import gdal
from ...settings import MASK_DIR
from PIL import Image


class MergeMask(Step):
    def process(self, data: dict, inputs: dict):
        height, width = self.read_tif(inputs["source_tiffile"])
        size = inputs["tile_size"]
        img = Image.new("RGB", (width, height))
        mask_dir = os.listdir(MASK_DIR)

        for mask_filename in mask_dir:
            im = Image.open(mask_filename)
            i = int(mask_filename[5])
            j = int(mask_filename[7])
            img.paste(im, (j * size, i * size))

        img.save("complete_mask.jpg")

    def read_tif(self, tif_path):
        ds = gdal.Open(tif_path)
        row = ds.RasterXSize
        col = ds.RasterYSize
        return row, col



