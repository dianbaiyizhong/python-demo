import json
import os

from image.ImageUtil import adjust_resolution, round_corners, extract_frames, fill_colors, pick_color, \
    extract_video_frames, crop_image, get_video_frames


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
    entries = get_imlist(f"/Users/huanghaoming/Documents/GitHub/nbawidgets/app/src/main/res/mipmap-xxhdpi")

    size = 0
    for item in entries:
        if 'simple' in item and ("_" + teamName) in item:
            size = size + 1

    size2015 = 0
    for item in entries:
        if '2016' not in item and 'simple' not in item and (teamName + "_") in item:
            size2015 = size2015 + 1
            old = teamName
            if 's76ers' in item:
                old = 's76ers'
            os.rename(item,
                      item.replace(f"hormovie_2015_nets_", f"movie_2015_hornets_"))

    # size2016 = 0
    # for item in entries:
    #     if '2016' in item and ("_" + teamName) in item:
    #         size2016 = size2016 + 1
    #         os.rename(item,
    #                   item.replace(f"frame_{teamName}_2016", f"movie_2016_{teamName}"))

    # _list.append({
    #     'teamName': teamName,
    #     'simpleFrameSize': size,
    #     'movie2015FrameSize': size2015,
    #     'movie2016FrameSize': size2016,
    # })

print(json.dumps(_list))
