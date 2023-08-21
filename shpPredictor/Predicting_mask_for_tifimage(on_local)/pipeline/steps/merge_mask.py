import os
from .step import Step
from osgeo import gdal
from shpPredictor.Project_Nanshang.pipeline.settings import MASK_DIR, COMPLETE_MASK_JPG
from PIL import Image


class MergeMask(Step):
    def process(self, data: dict, inputs: dict):
        width, height = self.read_tif(inputs["source_tiffile"])
        size = inputs["tile_size"]
        img = Image.new("RGB", (width, height))
        mask_dir = os.listdir(MASK_DIR)

        # collage small image to a complete image
        for mask_filename in mask_dir:
            im = Image.open(os.path.join(MASK_DIR, mask_filename))
            name_list = mask_filename[:-4].split("_")  # ex. turn mask_0_11.jpg into ['mask', '0', '11']
            i = int(name_list[1])  # the 1th value in name_list indicate the order in x ray
            j = int(name_list[2])  # the 2th value in name_list indicate the order in y ray
            img.paste(im, (i * size, j * size))   # see more detail in samgeo.common.split_raster())

        img.save(COMPLETE_MASK_JPG)
        return data

    def read_tif(self, tif_path):
        ds = gdal.Open(tif_path)
        width = ds.RasterXSize
        height = ds.RasterYSize
        return width, height

    def __str__(self):
        return "MergeMask"

