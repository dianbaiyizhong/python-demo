import os

from PIL import Image, ImageDraw, ImageSequence

import cv2

from pygifsicle import optimize


def remove_color(image_path, color_to_remove, output_path):
    # 打开图像
    image = Image.open(image_path).convert("RGBA")
    width, height = image.size

    # 获取图像的像素数据
    pixels = image.load()

    # 遍历每个像素
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]

            # 检查当前像素是否为要移除的颜色
            if (r, g, b) == color_to_remove:
                # 将该像素设置为透明
                pixels[x, y] = (0, 0, 0, 0)

    # 保存修改后的图像
    image.save(output_path, format="PNG")


def adjust_resolution(input_image_path, output_image_path, new_width, new_height):
    with Image.open(input_image_path) as image:
        resized_image = image.resize((new_width, new_height))
        resized_image.save(output_image_path)


def round_corners(image_path, output_path, radius):
    # 打开图片
    image = Image.open(image_path).convert("RGBA")
    # 创建一个与原图相同大小的空白图像
    mask = Image.new("RGBA", image.size, (0, 0, 0, 0))
    # 创建一个画笔
    draw = ImageDraw.Draw(mask)
    # 绘制圆角矩彤
    draw.rounded_rectangle((0, 0, image.width, image.height), radius, fill=(255, 255, 255))
    # 创建输出图片
    result = Image.new("RGBA", image.size)
    # 粘贴原图，遮罩用上面绘制的圆角图片
    result.paste(image, mask=mask)
    # 保存
    result.save(output_path)


def extract_video_frames(video_path, output_prefix):
    # 创建VideoCapture对象
    cap = cv2.VideoCapture(video_path)

    print(video_path)
    # 检查视频是否打开成功
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    # 帧计数器
    frame_count = 0

    # 读取视频帧
    while True:
        ret, frame = cap.read()

        # 如果正确读取帧，ret为True
        if not ret:
            print("Done: No frames remaining.")
            break

        # 保存图片到文件
        cv2.imwrite(f'{output_prefix}_{frame_count:0>5}.png', frame)

        # 更新帧计数器
        frame_count += 1

    # 释放VideoCapture对象
    cap.release()


def extract_frames(gif_path, output_prefix):
    with Image.open(gif_path) as gif:
        try:
            frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
        except IndexError:
            print(f"{gif_path} does not contain any frames.")
            return

        for index, frame in enumerate(frames):
            frame_path = f"{output_prefix}_{index}.png"
            os.makedirs(os.path.dirname(frame_path), exist_ok=True)
            frame.save(frame_path, "PNG")
            print(f"Frame {index} saved to {frame_path}")


def fill_colors(image_path, output_path, color):
    image = Image.open(image_path).convert("RGBA")
    left, top, right, bottom = 450, 450, 500, 500
    # 设置填充颜色为红色
    # 填充区域
    for i in range(left, right):
        for j in range(top, bottom):
            image.putpixel((i, j), color)

    left, top, right, bottom = 0, 0, 50, 50
    # 设置填充颜色为红色
    # 填充区域
    for i in range(left, right):
        for j in range(top, bottom):
            image.putpixel((i, j), color)

    left, top, right, bottom = 450, 0, 500, 50
    # 设置填充颜色为红色
    # 填充区域
    for i in range(left, right):
        for j in range(top, bottom):
            image.putpixel((i, j), color)

    left, top, right, bottom = 0, 450, 50, 500
    # 设置填充颜色为红色
    # 填充区域
    for i in range(left, right):
        for j in range(top, bottom):
            image.putpixel((i, j), color)

    # 保存修改后的图片
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)


def pick_color(image_path):
    # 打开图像文件
    image = Image.open(image_path)
    px = image.load()
    # 获取特定像素位置的颜色
    image = image.convert('RGB')
    color = image.getpixel((100, 100))
    return color


def crop_image(image_path, output_path, left, top, right, bottom):
    # 打开图片
    image = Image.open(image_path)
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)


def get_video_frames(video_path):
    # 使用cv2读取视频
    cap = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    # 获取视频的帧数
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f"Total number of frames: {frame_count}")

    # 释放视频对象
    cap.release()

    return frame_count


def merge_gif(file_name, size, key):
    images = []
    import imageio
    for i in range(size):
        if i % 2 == 0:
            images.append(f'{key}_{i:0>5}.png')
    # imageio.mimsave(file_name, images, duration=0.005, loop=0)

    # 设置GIF的参数
    fps = 15  # 帧率

    # 创建GIF
    with imageio.get_writer(file_name, fps=fps, loop=0) as writer:
        for image_file in images:
            image = imageio.imread(image_file)
            writer.append_data(image)


def crop_circle_from_image(image_path, output_path, center_x, center_y, radius):
    # 打开原始图片并转换为 RGBA 模式以支持透明度
    image = Image.open(image_path).convert("RGBA")

    # 创建一个与图像大小相同的空白（透明）图像作为遮罩
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)

    # 绘制圆形遮罩
    left_up_corner = (center_x - radius, center_y - radius)
    right_down_corner = (center_x + radius, center_y + radius)
    draw.ellipse([left_up_corner, right_down_corner], fill=255)

    # 创建一个新的透明图像来放置裁剪后的圆形区域
    output = Image.new("RGBA", image.size)

    # 将原始图像粘贴到新图像上，使用遮罩来定义可见区域
    output.paste(image, (0, 0), mask=mask)

    # 如果需要保存为圆形区域，可以裁剪图像到指定的圆形边界
    cropped_output = output.crop((center_x - radius, center_y - radius, center_x + radius, center_y + radius))

    # 保存结果图像
    cropped_output.save(output_path, "PNG")  # 确保保存为支持透明度的格式，如 PNG
    print(f"Circular area saved to {output_path}")


def add_hollow_cylinder(input_path, output_path, outer_radius, inner_radius, color=(255, 188, 0, 255)):
    """
    在图片中心添加通心圆柱体（圆环）

    参数:
        input_path: 输入图片路径
        output_path: 输出图片路径
        outer_radius: 外圆半径（像素）
        inner_radius: 内圆半径（像素）
        color: 圆环颜色 (R, G, B, A)，默认半透明白色
    """
    # 打开原始图片并转换为RGBA模式
    original = Image.open(input_path).convert("RGBA")
    width, height = original.size

    # 创建透明图层用于绘制圆环
    ring_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(ring_layer)

    # 计算中心坐标
    center_x, center_y = width // 2, height // 2

    # 绘制外圆（半透明填充）
    outer_bbox = (
        center_x - outer_radius,
        center_y - outer_radius,
        center_x + outer_radius,
        center_y + outer_radius
    )
    draw.ellipse(outer_bbox, fill=color)

    # 绘制内圆（透明填充，形成空心效果）
    inner_bbox = (
        center_x - inner_radius,
        center_y - inner_radius,
        center_x + inner_radius,
        center_y + inner_radius
    )
    draw.ellipse(inner_bbox, fill=(0, 0, 0, 0))

    # 合并原始图片和圆环图层
    result = Image.alpha_composite(original, ring_layer)
    result.save(output_path)
    print(f"处理完成，结果已保存至: {output_path}")
