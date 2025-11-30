import json
import os

from image.ImageUtil import adjust_resolution, round_corners, extract_frames, fill_colors, pick_color, \
    extract_video_frames, crop_image, get_video_frames, merge_gif

merge_gif("warriors.gif", 120, f"/Users/huanghaoming/Downloads/gif_frame/warriors/no_water/" + "simple_warriors")


# gif_path = f'warriors.gif'
# output_path = f'/Users/huanghaoming/Downloads/slow_frame/warriors'
# extract_frames(gif_path, output_path)
