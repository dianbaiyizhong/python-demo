import json
import os
import shutil

from PIL import Image, ImageDraw
from image.ImageUtil import adjust_resolution, round_corners, extract_frames, fill_colors, pick_color, \
    extract_video_frames, crop_image, get_video_frames, crop_circle_from_image, merge_gif

merge_gif("76ers.gif", 57, f"/Users/huanghaoming/Downloads/76/" + "nba_on_espn_76ers")
