import os

import cv2

from PIL import Image


def invert_image(input_path, output_path):
    # 打开图像文件
    image = Image.open(input_path).convert('RGB')  # 确保图像是 RGB 模式
    # 反转图像颜色
    inverted_image = Image.eval(image, lambda x: 255 - x)
    # 保存黑白反转后的图像
    inverted_image.save(output_path)
    print(f"Inverted image saved to {output_path}")


def convert_to_black_and_white_adaptive(input_path, output_path):
    # 读取图像并转换为灰度图像
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    # 应用自适应阈值方法
    _, bw_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 或者使用自适应阈值
    # bw_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # 保存黑白图像
    cv2.imwrite(output_path, bw_image)
    print(f"Black and white image saved to {output_path}")


def make_black_transparent(input_path, output_path):
    # 打开图像文件并转换为 RGBA 模式（确保有 Alpha 通道）
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    newData = []
    cutoff = 50  # 设置一个阈值，以决定哪些像素被认为是“黑色”

    for item in datas:
        # 如果是黑色（RGB 值都小于阈值），则设置为透明
        if item[0] <= cutoff and item[1] <= cutoff and item[2] <= cutoff:
            newData.append((255, 255, 255, 0))  # 设置为完全透明
        else:
            newData.append(item)  # 保持原来的颜色和透明度

    img.putdata(newData)
    img.save(output_path, "PNG")  # PNG 支持透明度
    print(f"Image with black made transparent saved to {output_path}")


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]


files_and_dirs = get_imlist('/Users/huanghaoming/Downloads/haws/')

# 使用sorted函数按字母顺序对文件和文件夹名称进行排序
sorted_files_and_dirs = sorted(files_and_dirs)
index = 0
for filename in sorted_files_and_dirs:
    input_image_path = filename
    output_image_path = f'/Users/huanghaoming/Downloads/haws/output/hornets_{index:0>3}.png'
    convert_to_black_and_white_adaptive(input_image_path, output_image_path)
    invert_image(output_image_path, output_image_path)
    make_black_transparent(output_image_path, output_image_path)
    index = index + 1
