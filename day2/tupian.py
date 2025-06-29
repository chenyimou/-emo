import numpy as np
from PIL import Image
import rasterio

def process_sentinel2(band_data, brightness=1.0):
    """
    处理哨兵2号数据，将5个波段转换为RGB三通道

    参数:
        band_data: numpy数组，形状为(5, height, width)，包含5个波段数据
                  顺序应为: [B4(红), B3(绿), B2(蓝), B8(近红外), B12(短红外)]
                  数值范围: 0-10000
        brightness: 亮度调整系数，默认1.0(原始亮度)，大于1增加亮度，小于1减小亮度

    返回:
        rgb_image: PIL Image对象，RGB三通道图像，数值范围0-255
    """
    # 1. 数据压缩到0-255范围
    compressed = (band_data / 10000 * 255).astype(np.uint8)

    # 2. 提取RGB三个波段 (B4,B3,B2)
    red = compressed[0]
    green = compressed[1]
    blue = compressed[2]

    # 3. 应用亮度调整 (限制在0-255范围内)
    red = np.clip(red * brightness, 0, 255).astype(np.uint8)
    green = np.clip(green * brightness, 0, 255).astype(np.uint8)
    blue = np.clip(blue * brightness, 0, 255).astype(np.uint8)

    # 4. 合并为RGB图像
    rgb_array = np.stack([red, green, blue], axis=-1)
    rgb_image = Image.fromarray(rgb_array)

    return rgb_image

def process_sentinel2_tif(tif_path, brightness=1.0):
    """
    处理哨兵2号TIFF文件

    参数:
        tif_path: TIFF文件路径
        brightness: 亮度调整系数，默认1.0(原始亮度)，大于1增加亮度，小于1减小亮度

    返回:
        rgb_image: PIL Image对象，RGB三通道图像
    """
    with rasterio.open(tif_path) as src:
        # 读取所有波段数据
        band_data = src.read()

        # 确保有5个波段
        if band_data.shape[0] != 5:
            raise ValueError("TIFF文件应包含5个波段(B4,B3,B2,B8,B12)")

        return process_sentinel2(band_data, brightness)

# 示例用法
if __name__ == "__main__":
    # 处理实际TIFF文件
    try:
        # 示例：增加20%亮度 (brightness=1.2)
        rgb_image = process_sentinel2_tif("2020_0427_fire_B2348_B12_10m_roi.tif", brightness=1.2)
        rgb_image.save("output_rgb.jpg")
        print("RGB图像已保存为output_rgb.jpg (亮度增加20%)")
    except Exception as e:
        print(f"处理失败: {e}")
