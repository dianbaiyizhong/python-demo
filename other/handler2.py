import os

from image.ImageUtil import crop_image

# path = "/Users/huanghaoming/Downloads/mipmap-xxhdpi"
# for filename in os.listdir(path):
#     crop_image(f"/Users/huanghaoming/Downloads/mipmap-xxhdpi/{filename}",
#                f"/Users/huanghaoming/Downloads/mipmap-xxhdpi/{filename}", 2, 0, 298, 69)


path = "/Users/huanghaoming/Downloads/logo"
for filename in os.listdir(path):
    os.rename(os.path.join(path, filename), os.path.join(path, "logo_" + filename))
