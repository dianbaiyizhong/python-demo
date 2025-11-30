# 定义一个方法，遍历某个目录下的所有png文件，要排序，并按照前缀重命名
#     output_image_path = f'/Users/huanghaoming/Downloads/haws/{index:03d}.png'
#     os.rename(input_image_path, output_image_path)
#     index += 1
#     print(f"Renamed {input_image_path} to {output_image_path}")
#   # invert_image(input_image_path, output_image_path)


import os
import re
from pathlib import Path


def rename_png_files(directory, prefix):
    """
    遍历指定目录下的所有 PNG 文件，按名称排序，并按照给定前缀重命名。

    :param directory: 要遍历的目录路径
    :param prefix: 用于新文件名的前缀
    """
    # 确保目录存在且为绝对路径
    directory = Path(directory).resolve()
    if not directory.is_dir():
        raise NotADirectoryError(f"The provided path '{directory}' is not a valid directory.")

    # 获取所有 PNG 文件并排序
    png_files = list(directory.glob('*.png'))

    # 如果需要根据文件名中的数字排序，可以使用正则表达式提取数字
    def extract_number(filename):
        match = re.search(r'(\d+)', filename.stem)
        return int(match.group(1)) if match else float('inf')  # 如果没有数字，默认排在最后

    png_files.sort(key=extract_number)

    # 重命名文件
    for index, old_path in enumerate(png_files, start=1):
        new_filename = f"{prefix}_{index:03d}.png"  # 使用三位数编号
        new_path = directory / new_filename

        # 确保不会覆盖已有的文件
        if new_path.exists():
            print(f"Warning: File {new_path} already exists. Skipping renaming of {old_path}.")
            continue

        try:
            old_path.rename(new_path)
            print(f'Renamed: {old_path.name} -> {new_filename}')
        except Exception as e:
            print(f'Failed to rename {old_path}: {e}')


# 使用示例
input_directory = '/Users/huanghaoming/Documents/GitHub/nba-watch-game/nba/bulls'
prefix = 'bulls'
rename_png_files(input_directory, prefix)
