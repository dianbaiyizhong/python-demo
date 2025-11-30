import json
import os

from image.ImageUtil import round_corners

# path = "/Users/huanghaoming/Downloads/76"
# for filename in os.listdir(path):
#     os.rename(os.path.join(path, filename), os.path.join(path, "s" + filename))


with open('logo.json', 'r') as file:
    data = json.load(file)
    for item in data:
        teamName = item['teamName']
        path = f'/Users/huanghaoming/Documents/nba_logo/2016/{teamName}'
        size = 0
        entries = os.listdir(path)
        # 使用 sorted 函数进行排序
        # 这里按照字符串的字典顺序进行排序
        sorted_entries = sorted(entries)
        print(teamName)
        for filename in sorted_entries:
            round_corners(os.path.join(path, filename), os.path.join(path, filename), 50)
            # os.rename(os.path.join(path, filename), os.path.join(path, f'frame_{teamName}_2016_{size:0>5}.png'))
            size = size + 1
        # for i in range(size):
