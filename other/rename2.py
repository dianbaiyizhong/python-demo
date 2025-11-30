import json
import os

from image.ImageUtil import round_corners

path = "/Users/huanghaoming/Downloads/tmp"
path2 = "/Users/huanghaoming/Downloads/tmp1"

files_and_dirs = os.listdir(path)

teamName = "jazz"
# 使用sorted函数按字母顺序对文件和文件夹名称进行排序
sorted_files_and_dirs = sorted(files_and_dirs)
index = 0
for filename in sorted_files_and_dirs:
    if 'jpg' in filename:
        print(filename)
        os.rename(os.path.join(path, filename), os.path.join(path2, f'movie_2016_{teamName}_{index:0>5}.jpg'))
        index = index + 1
        print(index)

# os.rename(os.path.join(path, filename), os.path.join(path, "s" + filename))
