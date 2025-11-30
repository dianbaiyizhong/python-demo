import os
import shutil

for i in range(142):
    path = f"/Users/huanghaoming/Documents/GitHub/nba-widgets/module-nba-2k16-circle/src/main/res/mipmap-xxhdpi/movie_2016_circle_warriors_{i:0>5}.png"
    if i % 3 == 0:
        shutil.copy(path, '/Users/huanghaoming/Downloads/movie/')


# i = 0
# for filename in os.listdir("/Documents/GitHub/nba-widgets/module-nba-2k16-circle/src/main/res/mipmap-xxhdpi"):
#     if "warrior" in filename:
#
#
