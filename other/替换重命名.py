import os
import shutil


def rename_files_with_pattern(directory, old_str, new_str):
    """
    将指定目录下所有文件名中包含 old_str 的部分替换为 new_str。

    :param directory: 要处理的目录路径
    :param old_str: 需要被替换的字符串
    :param new_str: 替换后的字符串
    """
    # 遍历指定目录下的所有文件和子目录
    for filename in os.listdir(directory):
        # 构建完整的文件路径
        filepath = os.path.join(directory, filename)

        # 如果是文件并且文件名中包含 old_str，则进行重命名
        if os.path.isfile(filepath) and old_str in filename:
            # 构造新的文件名
            new_filename = filename.replace(old_str, new_str)
            new_filepath = os.path.join(directory, new_filename)

            print(f'Renaming "{filename}" to "{new_filename}"')
            # 重命名文件
            shutil.move(filepath, new_filepath)


# 使用示例
directory_path = '/Users/huanghaoming/Documents/GitHub/nba-watch-face/watch-face-studio-project/timberwolves_res/upscayl_png_realesrgan-x4plus-anime_2x/'  # 替换为你的目录路径
old_string = 'warriors'  # 要替换的字符串
new_string = 'timberwolves'  # 替换后的字符串

rename_files_with_pattern(directory_path, old_string, new_string)
