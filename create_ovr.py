import os
from osgeo import gdal

# 定义处理栅格数据的函数
def create_ovr(file_path):
    dataset = gdal.Open(file_path, gdal.GA_Update)
    if dataset is None:
        print(f"无法打开文件 {file_path}")
        return
    gdal.SetConfigOption('USE_RRD', 'YES')
    gdal.SetConfigOption('COMPRESS_OVERVIEW', 'DEFLATE')  # 设置压缩方式
    dataset.BuildOverviews('NEAREST', [32, 64, 128])
    # dataset.BuildOverviews('NEAREST', [1, 2, 4, 8, 16])
    dataset = None
    print(f"已处理文件 {file_path}")

# 定义要遍历的文件夹路径
folder_path = 'D:\geodl\hecy\数据\第二批'

# process_raster("D:\geodl\hecy\数据\第二批\E121D4_N31D9_20220411_GF2_DOM_4_fus\E121D4_N31D9_20220411_GF2_DOM_4_fus.tif")
for subdir, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".tif"):
            file_path = os.path.join(subdir, filename)

            create_ovr(file_path)
