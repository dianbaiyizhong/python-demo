from pathlib import Path

from image.ImageUtil import round_corners


def find_png_files(directory):
    """
    遍历指定目录及其所有子目录下的所有 PNG 文件。

    :param directory: 要遍历的根目录路径
    :return: 包含所有 PNG 文件路径的生成器
    """
    # 确保目录存在且为绝对路径
    directory = Path(directory).resolve()
    if not directory.is_dir():
        raise NotADirectoryError(f"The provided path '{directory}' is not a valid directory.")

    # 使用 rglob 递归查找所有 PNG 文件
    return directory.rglob('*.png')


# 使用示例
input_directory = '/Users/huanghaoming/Downloads/未命名文件夹 2'

try:
    png_files = find_png_files(input_directory)
    for png_file in png_files:
        print(png_file)  # 或者对每个文件执行其他操作
        round_corners(png_file, png_file, 50)
except NotADirectoryError as e:
    print(e)
