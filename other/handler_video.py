from video.VideoUtil import process_video

# 使用示例
input_video_path = '卡普起身mask.mp4'
output_video_path = '卡普起身mask_o.mp4'
process_video(input_video_path, output_video_path, corner_size=0.3)  # 将右下角 30% 区域设置为黑色
