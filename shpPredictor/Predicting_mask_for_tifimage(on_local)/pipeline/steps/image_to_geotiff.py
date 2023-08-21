from .step import Step
from shpPredictor.Project_Nanshang.pipeline.settings import COMPLETE_MASK_JPG,  COMPLETE_MASK_TIFF,  COMPLETE_MASK_GEOTIFF
import aspose.words as aw
from rasterio.transform import from_origin
import rasterio


class Image2Geotiff(Step):
    def process(self, data: dict, inputs: dict):
        self.jpg2tiff()
        self.tiff2goetiff(inputs["below_right_lat"], inputs["top_left_lat"],
                          inputs["below_right_lon"], inputs["top_left_lon"])
        return data

    def jpg2tiff(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        shape = builder.insert_image(COMPLETE_MASK_JPG)
        shape.image_data.save(COMPLETE_MASK_TIFF)

    def tiff2goetiff(self, below_right_lat, top_left_lat, below_right_lon, top_left_lon):
        # Read the input TIFF
        with rasterio.open(COMPLETE_MASK_GEOTIFF) as src:
            data = src.read()
            dtype = src.dtypes[0]
            count = src.count
            height, width = src.height, src.width

        # compute horizontal pixel size and vertical pixel size in degrees
        dis_lat = below_right_lat - top_left_lat
        dis_lon = below_right_lon - top_left_lon
        pixel_size_x = dis_lon / width  # Example: horizontal pixel size in degrees
        pixel_size_y = dis_lat / height  # Example: vertical pixel size in degrees

        # Define geospatial information
        crs = 'EPSG:4326'  # Example: WGS 84

        # Define the geotransform
        transform = from_origin(top_left_lon, top_left_lat, pixel_size_x, pixel_size_y)

        # Write the GeoTIFF file
        with rasterio.open(
                COMPLETE_MASK_GEOTIFF,
                'w',
                driver='GTiff',
                height=height,
                width=width,
                count=count,
                dtype=dtype,
                crs=crs,
                transform=transform,
        ) as dst:
            dst.write(data)

    def __str__(self):
        return "Image2Geotiff"



