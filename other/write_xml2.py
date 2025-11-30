import json
import os

from image.ImageUtil import adjust_resolution, round_corners, extract_frames, fill_colors, pick_color, \
    extract_video_frames, crop_image, get_video_frames, merge_gif


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("文件不存在")


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]


with open('logo.json', 'r') as file:
    data = json.load(file)

_list = list()
# 遍历数组
for item in data:
    teamName = item['teamName']
    color = pick_color(path + f"simple_{teamName}_000.png")
    hex_code = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
    print(hex_code)
    item['bgColor'] = hex_code

    for i in range(simpleFrameSize):
        fill_colors(path + f"simple_{teamName}_{i:0>3}.png", path + f"simple_{teamName}_{i:0>3}.png", color)
    merge_gif("gif_" + teamName + ".gif", simpleFrameSize, path + "simple_" + teamName)

print(json.dumps(data))