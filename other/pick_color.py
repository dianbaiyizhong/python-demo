import glob
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
    entries = get_imlist('/Users/huanghaoming/Downloads/tmp2')
    for filename in entries:
        if teamName.lower() in filename.lower():
            print(filename)
            color = pick_color(f"{filename}")
            hex_code = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
            item['scoreBoardColor'] = hex_code
            print(hex_code)

            break

print(json.dumps(data, ensure_ascii=False))
