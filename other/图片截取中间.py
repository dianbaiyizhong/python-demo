import os

import cv2

from PIL import Image

from PIL import Image


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


files_and_dirs = get_imlist('/Users/huanghaoming/Downloads/country/')

# 使用sorted函数按字母顺序对文件和文件夹名称进行排序
sorted_files_and_dirs = sorted(files_and_dirs)
index = 0
for input_image_path in sorted_files_and_dirs:
    filename = os.path.basename(input_image_path)
    output_image_path = f'/Users/huanghaoming/Downloads/country/output/country_{filename}.png'
    print(input_image_path)
    # 打开图片
    image = Image.open(input_image_path)

    # 原始图片的尺寸
    original_width, original_height = image.size

    # 计算截取区域的起始坐标
    # 宽度和高度的一半（向下取整）
    start_width = original_width
    start_height = (original_height - 750) // 2

    # 截取中间部分
    print(start_width, start_height)
    cropped_image = image.crop((0, 0, start_width, original_height - 40))

    # 显示截取后的图片（可选）
    # cropped_image.show()

    # 保存截取后的图片（可选）
    cropped_image.save(output_image_path)
