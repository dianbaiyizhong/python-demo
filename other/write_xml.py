import json
from image.ImageUtil import adjust_resolution, round_corners, extract_frames, fill_colors, pick_color, \
    extract_video_frames, crop_image, get_video_frames


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("文件不存在")


with open('logo.json', 'r') as file:
    data = json.load(file)

# 遍历数组
for item in data:
    teamName = item['teamName']
    size = item['movie2015FrameSize']
    for i in range(size):
        source_img = f'/Users/huanghaoming/Documents/GitHub/nba-widgets/module-nba-2k15/src/main/res/mipmap-xxhdpi/movie_2015_{teamName}_{i:0>5}.png'
        output_img = f'/Users/huanghaoming/Documents/GitHub/nba-widgets/module-nba-2k15/src/main/res/mipmap-xxhdpi/movie_2015_circle_{teamName}_{i:0>5}.png'
        round_corners(source_img, output_img, 250)
