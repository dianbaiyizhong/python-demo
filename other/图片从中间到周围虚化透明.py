import math
import os

import cv2
import numpy as np

from PIL import Image, ImageDraw, ImageFilter

from PIL import Image


def center_blur_transparent(input_path, output_path, blur_radius=20, fade_range=0.5):
    # 打开图片
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size

    # 创建渐变蒙版（中心白，边缘黑）
    mask = Image.new("L", (width, height), 0)  # L 模式表示灰度图
    draw = ImageDraw.Draw(mask)

    # 计算渐变范围（椭圆）
    center = (width // 2, height // 2)
    max_radius = ((width ** 2 + height ** 2) ** 0.5) / 2  # 最大半径（对角线一半）
    fade_radius = max_radius * fade_range  # 渐变范围

    # 绘制径向渐变（从中心到边缘）
    for y in range(height):
        for x in range(width):
            distance = ((x - center[0]) ** 2 + (y - center[1]) ** 2) ** 0.5
            alpha = max(0, min(255, int(255 * (1 - distance / fade_radius))))
            mask.putpixel((x, y), alpha)

    # 应用模糊（仅模糊非透明部分）
    blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))

    # 合并原图和模糊图（根据蒙版渐变）
    final_img = Image.new("RGBA", (width, height))
    final_img = Image.composite(img, blurred_img, mask)

    # 保存结果
    final_img.save(output_path, "PNG")


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png') or f.endswith('.jpg')]


def left_semi_circle_transparency_opencv(input_path, output_path, fade_range=0.7):
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if img.shape[2] == 3:  # 如果没有 Alpha 通道，转为 BGRA
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    height, width = img.shape[:2]

    # 创建坐标网格（向量化计算）
    x = np.arange(width)
    y = np.arange(height)
    xx, yy = np.meshgrid(x, y)

    # 计算中心点
    center_x, center_y = width // 2, height // 2
    max_radius = min(center_x, center_y)
    fade_radius = max_radius * fade_range

    # 计算距离和角度
    dx = xx - center_x
    dy = yy - center_y
    distance = np.sqrt(dx ** 2 + dy ** 2)
    angle = np.degrees(np.arctan2(dy, dx))

    # 创建 Alpha 通道（左侧半圆渐变）
    alpha = np.zeros((height, width), dtype=np.uint8)
    mask = (distance <= fade_radius) & (angle >= -90) & (angle <= 90)  # 左侧半圆条件
    alpha[mask] = (255 * (1 - distance[mask] / fade_radius)).astype(np.uint8)

    # 应用 Alpha 通道
    img[:, :, 3] = alpha
    cv2.imwrite(output_path, img)


def adaptive_radial_transparency(input_path, output_path, fade_strength=1.0):
    """
    使图片从中心到边缘逐渐透明，并自适应调整渐变方式
    :param input_path: 输入图片路径
    :param output_path: 输出图片路径（PNG）
    :param fade_strength: 渐变强度（0~1，值越大边缘越透明）
    """
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size

    # 判断图片方向（纵向 or 横向）
    is_portrait = height > width

    # 创建 Alpha 通道蒙版（中心 255，边缘 0）
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)

    center = (width // 2, height // 2)

    # 计算渐变范围（椭圆渐变）
    max_radius_x = width / 2  # X 方向最大半径
    max_radius_y = height / 2  # Y 方向最大半径

    # 调整渐变计算方式（纵向图片让 Y 方向渐变更快）
    if is_portrait:
        radius_scale_x = 1.0  # X 方向渐变正常
        radius_scale_y = 0.6  # Y 方向渐变更快（值越小，顶部/底部越早透明）
    else:
        radius_scale_x = 0.6  # X 方向渐变更快（值越小，左右越早透明）
        radius_scale_y = 1.0  # Y 方向渐变正常

    # 计算每个像素的 Alpha 值
    for y in range(height):
        for x in range(width):
            # 计算归一化距离（椭圆渐变）
            dx = (x - center[0]) / (max_radius_x * radius_scale_x)
            dy = (y - center[1]) / (max_radius_y * radius_scale_y)
            distance = (dx ** 2 + dy ** 2) ** 0.5  # 椭圆渐变

            # 计算 Alpha（0~255）
            alpha = max(0, min(255, int(255 * (1 - distance * fade_strength))))
            mask.putpixel((x, y), alpha)

    # 应用 Alpha 通道
    img.putalpha(mask)
    img.save(output_path, "PNG")


def radial_transparency(input_path, output_path, fade_range=0.7):
    """
    使图片从中心到边缘逐渐透明
    :param input_path: 输入图片路径
    :param output_path: 输出图片路径（PNG）
    :param fade_range: 渐变范围（0~1，越大渐变越平缓）
    """
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size

    # 创建 Alpha 通道蒙版（中心 255，边缘 0）
    mask = Image.new("L", (width, height), 0)  # L 模式 = 8-bit 灰度
    draw = ImageDraw.Draw(mask)

    center = (width // 2, height // 2)
    max_radius = ((width ** 2 + height ** 2) ** 0.5) / 2  # 最大半径（对角线一半）
    fade_radius = max_radius * fade_range  # 渐变范围

    # 绘制径向渐变（中心白，边缘黑）
    for y in range(height):
        for x in range(width):
            distance = ((x - center[0]) ** 2 + (y - center[1]) ** 2) ** 0.5
            alpha = max(0, min(255, int(255 * (1 - distance / fade_radius))))
            mask.putpixel((x, y), alpha)

    # 应用 Alpha 通道
    img.putalpha(mask)
    img.save(output_path, "PNG")


files_and_dirs = get_imlist('/Users/huanghaoming/Downloads/area')

# 使用sorted函数按字母顺序对文件和文件夹名称进行排序
sorted_files_and_dirs = sorted(files_and_dirs)
index = 0
for input_image_path in sorted_files_and_dirs:
    filename = os.path.basename(input_image_path)
    output_image_path = f'/Users/huanghaoming/Downloads/area/output/{filename}'
    print(input_image_path)
    left_semi_circle_transparency_opencv(input_image_path, output_image_path, fade_range=0.7)
