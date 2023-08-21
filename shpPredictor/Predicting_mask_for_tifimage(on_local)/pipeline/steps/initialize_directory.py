from .step import Step
from shpPredictor.Project_Nanshang.pipeline.settings import OUTPUT_DIR, STOREHOUSE, SPLITED_TIFS_DIR, MASK_DIR
import os
import shutil


class InitializeDir(Step):
    def process(self, data: dict, inputs: dict):
        self.reinitialize_storehouse()
        self.checkOUTPUT_DIR()
        return data

    def reinitialize_storehouse(self):
        if os.path.exists(STOREHOUSE):
            shutil.rmtree(STOREHOUSE)
        os.mkdir(STOREHOUSE)
        os.mkdir(SPLITED_TIFS_DIR)
        os.mkdir(MASK_DIR)

    def checkOUTPUT_DIR(self):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    def __str__(self):
        return "InitializeDir"
