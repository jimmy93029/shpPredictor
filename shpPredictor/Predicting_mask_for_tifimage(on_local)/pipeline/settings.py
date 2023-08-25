import os


STOREHOUSE = "storehouse"
SPLITED_TIFS_DIR = os.path.join(STOREHOUSE, "splited_tifs")
MASK_DIR = os.path.join(STOREHOUSE, "masks")

complete_mask_filename = "map_mask"
COMPLETE_MASK_JPG = os.path.join(STOREHOUSE, complete_mask_filename + ".jpg")
COMPLETE_MASK_TIFF = os.path.join(STOREHOUSE, complete_mask_filename + ".tiff")
COMPLETE_MASK_GEOTIFF = os.path.join(STOREHOUSE, "geo" + complete_mask_filename + ".tiff")

OUTPUT = os.path.join(STOREHOUSE, "output")
