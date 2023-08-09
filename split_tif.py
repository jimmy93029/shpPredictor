from tqdm import tqdm
from osgeo import gdal
import numpy as np
from glob import glob
import os


def read_tif(tif_path):
    ds = gdal.Open(tif_path)
    row = ds.RasterXSize
    col = ds.RasterYSize
    band = ds.RasterCount
    print("opening")

    for i in range(band):
        data = ds.GetRasterBand(i+1).ReadAsArray()

        data = np.expand_dims(data , 2)
        if i == 0:
            allarrays = data
        else:
            allarrays = np.concatenate((allarrays, data), axis=2)

        print(i)
    return {'data':allarrays,'transform':ds.GetGeoTransform(),'projection':ds.GetProjection(),'bands':band,'width':row,'height':col}
    # 左上角点坐标 GeoTransform[0],GeoTransform[3] Transform[1] is the pixel width, and Transform[5] is the pixel height


def write_tif(fn_out, im_data, transform,proj=None):
    
    """
    功能:
    ----------
    将矩阵按某种投影写入tif，需指定仿射变换矩阵，可选渲染为rgba
    
    参数:
    ----------
    fn_out:str
        输出tif图的绝对文件路径
    im_data: np.array
        tif图对应的矩阵
    transform: list/tuple 
        gdal-like仿射变换矩阵，若im_data矩阵起始点为左上角且投影为4326，则为
            (lon_x.min(), delta_x, 0, 
             lat_y.max(), 0, delta_y)
    proj: str（wkt格式）
        投影，默认投影坐标为4326，可用osr包将epsg转化为wkt格式，如
            srs = osr.SpatialReference()# establish encoding
            srs.ImportFromEPSG(4326)    # WGS84 lat/lon
            proj = srs.ExportToWkt()    # create wkt fromat of proj
    """


    # 设置投影，proj为 wkt format
    if proj is None:
        proj = 'GEOGCS["WGS 84",\
                     DATUM["WGS_1984",\
                             SPHEROID["WGS 84",6378137,298.257223563, \
                                    AUTHORITY["EPSG","7030"]], \
                             AUTHORITY["EPSG","6326"]], \
                     PRIMEM["Greenwich",0, \
                            AUTHORITY["EPSG","8901"]], \
                     UNIT["degree",0.0174532925199433, \
                            AUTHORITY["EPSG","9122"]],\
                     AUTHORITY["EPSG","4326"]]'
    # 渲染为rgba矩阵
    # 设置数据类型
    if 'int8' in im_data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in im_data.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32
    # 将(通道数、高、宽)顺序调整为(高、宽、通道数)
    # print('shape of im data:', im_data.shape)
    im_bands = min(im_data.shape)
    im_shape = list(im_data.shape)
    im_shape.remove(im_bands)
    im_height, im_width = im_shape
    band_idx = im_data.shape.index(im_bands)
    # 找出波段是在第几个

    # 创建文件
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(fn_out, im_width, im_height, im_bands, datatype)
    print(dataset)

    # if dataset is not None:
    dataset.SetGeoTransform(transform)  # 写入仿射变换参数
    dataset.SetProjection(proj)  # 写入投影

    if im_bands == 1:

        # print(im_data[:, 0,:].shape)
        if band_idx == 0:
            dataset.GetRasterBand(1).WriteArray(im_data[0, :, :])
        elif band_idx == 1:
            dataset.GetRasterBand(1).WriteArray(im_data[:, 0, :])
        elif band_idx == 2:
            dataset.GetRasterBand(1).WriteArray(im_data[:, :, 0])

    else:

        for i in range(im_bands):
            if band_idx == 0:
                dataset.GetRasterBand(i + 1).WriteArray(im_data[i, :, :])
            elif band_idx == 1:
                dataset.GetRasterBand(i + 1).WriteArray(im_data[:, i, :])
            elif band_idx == 2:
                dataset.GetRasterBand(i + 1).WriteArray(im_data[:, :, i])

    dataset.FlushCache()
    del dataset
    driver = None



def split(origin_data,origin_transform,output_size,dirname):
    os.mkdir(f"{dirname}")
    origin_size = origin_data.shape
    # output_size[0] = 400
    # output_size[1] = 400
    x = origin_transform[0]
    y = origin_transform[3]
    x_step = origin_transform[1]
    y_step = origin_transform[5]
    output_x_step = x_step
    output_y_step = y_step
    for i in range(origin_size[0]//output_size[0]):
        for j in range(origin_size[1]//output_size[1]):
            output_data = origin_data[i * output_size[0]:(i+1) * output_size[0], j * output_size[1]:(j+1) * output_size[1] ,:]
            output_transform = (x + j * output_x_step * output_size[0], output_x_step,0, y + i* output_y_step *output_size[0], 0, output_y_step)

            write_tif(f'test3/{i}_{j}.tif', output_data, output_transform)
            print(f"finish test3/{i}_{j}.tif")


# read tiff file
print("into")
data = read_tif('NanShang_Tomb3.tif')
print("finishing data reading")

# please specify the dirname you want to make ,and the output size of your picture 
cwd = os.getcwd()
dirname = os.path.join(cwd, "test3") 
output_size = [700, 700]

# strat splitting 
split(origin_data=data['data'],origin_transform=data['transform'], output_size=output_size, dirname=dirname)
print("all finishing")
