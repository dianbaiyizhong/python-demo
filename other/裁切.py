import os

from PIL import Image


def crop_transparent(image_path, output_path):
    """裁切透明图片的透明边缘"""
    image = Image.open(image_path)

    # 确保图片有alpha通道
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    # 获取非透明区域的边界框
    bbox = image.getbbox()

    if bbox:
        cropped = image.crop(bbox)
        cropped.save(output_path, 'PNG')
        return cropped
    else:
        print("图片完全透明")
        return image


if __name__ == '__main__':
    for filename in os.listdir('logo/'):
        input_path = os.path.join('logo/', filename)
        output_path = os.path.join('logo_out/', filename)
        crop_transparent(input_path, output_path)
