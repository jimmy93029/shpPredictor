import rasterio
from rasterio.transform import from_origin
import numpy as np


# Input and output file paths
input_filename = "mask_6_3.tiff"

input_tiff_path = input_filename
output_geotiff_path = "geo" + input_filename


# Read the input TIFF
with rasterio.open(input_tiff_path) as src:
    data = src.read()
    dtype = src.dtypes[0]
    count = src.count
    height, width = src.height, src.width


 # 左上角、右下角的座標都需要定義
ori_top_left_y = 22.97494    # Example: latitude  
ori_top_left_x = 120.19544   # Example: longitude
ori_below_right_y = 22.96717    
ori_below_right_x = 120.19775  


dis_lat = ori_below_right_y - ori_top_left_y
dis_lon = ori_below_right_x - ori_top_left_x 

top_left_y = dis_lat / 32 * 6 + ori_top_left_y
top_left_x = dis_lon / 8 * 3 + ori_top_left_x

# Define geospatial information
crs = 'EPSG:4326'  # Example: WGS 84

pixel_size_x = dis_lon / 8 / width   # Example: horizontal pixel size in degrees
pixel_size_y = dis_lat / 32 / height  # Example: vertical pixel size in degrees

# Define the geotransform
transform = from_origin(top_left_x, top_left_y, pixel_size_x, pixel_size_y)

# Write the GeoTIFF file
with rasterio.open(
        output_geotiff_path,
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

print("Conversion completed successfully.")