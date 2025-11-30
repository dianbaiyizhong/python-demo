import os
import cv2
from pathlib import Path


def crop_images_right_two_thirds_advanced(input_dir, output_dir, quality=95):
    """
    增强版：截取输入目录中所有图片的右边三分之二部分

    Args:
        input_dir: 输入图片目录路径
        output_dir: 输出图片目录路径
        quality: JPEG图片质量 (1-100)
    """
    # 创建输出目录
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # 支持的图片格式
    supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}

    # 获取所有图片文件（包括子目录）
    image_files = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if Path(file).suffix.lower() in supported_formats:
                # 保持相对路径结构
                rel_path = os.path.relpath(root, input_dir)
                if rel_path == '.':
                    image_files.append((file, ''))
                else:
                    image_files.append((file, rel_path))

    if not image_files:
        print(f"在目录 '{input_dir}' 中没有找到图片文件")
        return

    print(f"找到 {len(image_files)} 个图片文件")

    processed_count = 0
    failed_count = 0

    for filename, rel_path in image_files:
        try:
            # 构建完整的文件路径
            if rel_path:
                input_path = os.path.join(input_dir, rel_path, filename)
                output_subdir = os.path.join(output_dir, rel_path)
                Path(output_subdir).mkdir(parents=True, exist_ok=True)
                output_path = os.path.join(output_subdir, filename)
            else:
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, filename)

            # 读取图片
            img = cv2.imread(input_path)
            if img is None:
                print(f"无法读取图片: {os.path.join(rel_path, filename) if rel_path else filename}")
                failed_count += 1
                continue

            # 获取图片尺寸
            height, width = img.shape[:2]

            # 计算右边三分之二的区域
            start_x = width // 3
            end_x = width

            # 截取右边三分之二区域
            cropped_img = img[0:height, start_x:end_x]

            # 根据文件扩展名设置保存参数
            file_ext = Path(filename).suffix.lower()
            save_params = []

            if file_ext in ['.jpg', '.jpeg']:
                save_params = [cv2.IMWRITE_JPEG_QUALITY, quality]
            elif file_ext == '.png':
                save_params = [cv2.IMWRITE_PNG_COMPRESSION, 9 - (quality // 11)]

            # 保存图片
            if save_params:
                cv2.imwrite(output_path, cropped_img, save_params)
            else:
                cv2.imwrite(output_path, cropped_img)

            original_size = f"{width}x{height}"
            new_size = f"{cropped_img.shape[1]}x{cropped_img.shape[0]}"
            file_path = os.path.join(rel_path, filename) if rel_path else filename
            print(f"✓ 处理成功: {file_path} ({original_size} -> {new_size})")
            processed_count += 1

        except Exception as e:
            file_path = os.path.join(rel_path, filename) if rel_path else filename
            print(f"✗ 处理失败: {file_path} - 错误: {str(e)}")
            failed_count += 1

    # 输出总结
    print(f"\n=== 处理总结 ===")
    print(f"成功处理: {processed_count} 个文件")
    print(f"处理失败: {failed_count} 个文件")
    print(f"输入目录: {input_dir}")
    print(f"输出目录: {output_dir}")


# 使用PIL库的替代版本（如果不想用OpenCV）
from PIL import Image


def crop_images_pil(input_dir, output_dir):
    """
    使用PIL库截取图片右边三分之二
    """
    from PIL import Image

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
    image_files = [f for f in os.listdir(input_dir)
                   if Path(f).suffix.lower() in supported_formats]

    for filename in image_files:
        # if 'hawks' not in filename:
        #     print(f"跳过文件: {filename}")
        #     continue
        try:
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with Image.open(input_path) as img:
                width, height = img.size

                # 计算右边三分之二区域
                left = width // 3
                right = width
                top = 0
                bottom = height

                # 裁剪图片
                cropped_img = img.crop((left, top, right, bottom))

                # 保存图片（保持原始格式）
                cropped_img.save(output_path)

                print(f"✓ 处理成功: {filename}")

        except Exception as e:
            print(f"✗ 处理失败: {filename} - 错误: {str(e)}")


def main():
    # 设置输入和输出目录
    input_directory = "nba_team_images"  # 替换为你的输入目录
    output_directory = "nba_team_images_cropped"  # 替换为你的输出目录

    # 选择使用哪个版本
    print("选择处理方式:")
    print("1. 使用OpenCV (推荐)")
    print("2. 使用PIL")

    crop_images_pil(input_directory, output_directory)

    # choice = input("请输入选择 (1 或 2): ").strip()
    #
    # if choice == "2":
    #     crop_images_pil(input_directory, output_directory)
    # else:
    #     crop_images_right_two_thirds_advanced(input_directory, output_directory)


if __name__ == "__main__":
    main()
