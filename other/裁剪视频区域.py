import cv2
from moviepy import VideoFileClip

# 输入和输出视频路径
input_video = "/Users/huanghaoming/Documents/新闻视频工作空间/2025080401.mp4"
output_video = "/Users/huanghaoming/Documents/新闻视频工作空间/2025080401_1.mp4"
output_video2 = "/Users/huanghaoming/Documents/新闻视频工作空间/2025080401_2.mp4"

# 裁剪区域 (x, y, width, height)
x, y = 362, 189  # 起始坐标
w, h = 1300, 675  # 裁剪宽度和高度

# 打开视频
cap = cv2.VideoCapture(input_video)

# 获取原视频的帧率和尺寸
fps = int(cap.get(cv2.CAP_PROP_FPS))
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 检查裁剪区域是否超出视频范围
if x + w > original_width or y + h > original_height:
    raise ValueError("裁剪区域超出视频范围！")

# 创建 VideoWriter 对象（输出裁剪后的视频）
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (w, h))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 裁剪帧
    cropped_frame = frame[y:y + h, x:x + w]

    # 写入输出视频
    out.write(cropped_frame)

    # 显示实时效果（可选）
    # cv2.imshow("Cropped Video", cropped_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print(f"视频裁剪完成！保存至: {output_video}")

# 加载视频
clip = VideoFileClip(output_video)

# 裁剪前 20 秒（如果视频不足 20 秒，则截取全部）
cropped_clip = clip.subclipped(3, 20)

# 保存裁剪后的视频
cropped_clip.write_videofile(output_video2, codec="libx264")

print(f"视频前 20 秒已保存至: {output_video2}")

