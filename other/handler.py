import json
import os
import shutil

from PIL import Image, ImageDraw
from image.ImageUtil import adjust_resolution, round_corners, extract_frames, fill_colors, pick_color, \
    extract_video_frames, crop_image, get_video_frames, crop_circle_from_image


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("文件不存在")


# for i in range(121):
#     path = f'/Users/huanghaoming/Documents/nba_logo/gif_frame/warriors/warriors_{i}.png'
#     out_path = f'/Users/huanghaoming/Documents/nba_logo/gif_frame/warriors/no_water/simple_warriors_{i:0>3}.png'
#     fill_colors(path, out_path)


# 读取JSON文件
with open('logo.json', 'r') as file:
    data = json.load(file)

# for filename in os.listdir("/Users/huanghaoming/Documents/nba_logo/video_pic"):
# adjust_resolution(f"/Users/huanghaoming/Documents/nba_logo/video_pic/{filename}",
#                   f"/Users/huanghaoming/Documents/nba_logo/video_pic/{filename}", 500, 500)
# crop_image(f"/Users/huanghaoming/Documents/nba_logo/video_pic/{filename}",
#            f"/Users/huanghaoming/Documents/nba_logo/video_pic/{filename}", 0, 0, 1080, 1080)
# source_img = f"/Users/huanghaoming/Documents/nba_logo/video_pic/{filename}"
# output_img = f"/Users/huanghaoming/Documents/nba_logo/video_pic/{filename}"
# round_corners(source_img, output_img, 50)
# for i in range(120):
# path = f"/Users/huanghaoming/Documents/GitHub/nba-watch-face/warriors_res/simple_circle_warriors_{i:0>3}.png"
# crop_circle_from_image(path,
#                        f"/Users/huanghaoming/Documents/GitHub/nba-watch-face/warriors_res/output/simple_circle_warriors_{i:0>3}.png",
#                        251, 243, 144)

# team_name = "warriors"
# for i in range(570, 628):
#     path = f"/Users/huanghaoming/Documents/GitHub/nba-watch-face/movie_{team_name}/movie_{team_name}_{i:0>5}.png"
#     if i % 2 == 0:
#         shutil.copy(path,
#                     f"/Users/huanghaoming/Documents/GitHub/nba-watch-face/movie_{team_name}/output/movie_{team_name}_{i:0>5}.png")

# for i in range(0, 251):
#     path = f"/Users/huanghaoming/Documents/GitHub/nba-watch-face/movie_celtics/movie_2016_circle_celtics_{i:0>5}.png"
#     if not os.path.exists(path):
#         continue
#     crop_circle_from_image(path,
#                            f"/Users/huanghaoming/Documents/GitHub/nba-watch-face/movie_celtics/output/simple_circle_celtics_{i:0>5}.png",
#                            250, 250, 240)

# 遍历数组
# for item in data:
#     teamName = item['teamName']
#     # print(teamName)
#     gif_path = f'warriors.gif'
#     output_path = f'/Users/huanghaoming/Documents/nba_logo/gif_frame/{teamName}/{teamName}'
#     extract_frames(gif_path, output_path)

# teamPath = f'/Users/huanghaoming/Documents/nba_logo/gif_frame/{teamName}/'
# fill_color = None
# size = 0
# for filename in os.listdir(teamPath):
#     fill_color = pick_color(image_path=teamPath + filename)
#     break
# for filename in os.listdir(teamPath):
#     if 'png' in filename:
#         size = size + 1
# _tmp = ""
# for i in range(size):
#     _tmp = _tmp + f'           <ImageView android:layout_width="match_parent" android:layout_height="wrap_content" android:src="@mipmap/simple_{teamName}_{i:0>3}" />'
# tmpl = read_file("template_bg.xml")
# tmpl = tmpl.replace("######", item['scoreBoardColor'])
# with open(f'xml/gradient_{teamName}_background.xml', 'w') as file:
#     file.write(tmpl)  # 将内容写入文件
# extract_video_frames(f'/Users/huanghaoming/Documents/nba_logo/mp4/{teamName}.mp4',
#                      f'/Users/huanghaoming/Documents/nba_logo/video_pic/{teamName}')

# for i in range(size):
#     source_img = f'/Users/huanghaoming/Documents/GitHub/nbawidgets/app/src/main/res/mipmap-xxhdpi/simple_{teamName}_{i:0>3}.png'
#     output_img = f'/Users/huanghaoming/Documents/GitHub/nbawidgets/app/src/main/res/mipmap-xxhdpi/simple_{teamName}_{i:0>3}.png'
#     round_corners(source_img, output_img, 50)

# out_path = f'/Users/huanghaoming/Documents/nba_logo/gif_frame/no_water/simple_{teamName}_{i:0>3}.png'
# fill_colors(teamPath + teamName + "_" + str(i) + ".png", out_path, fill_color)
