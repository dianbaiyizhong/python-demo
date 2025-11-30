import cv2
import numpy as np


def apply_mosaic(img, x, y, width, height, mosaic_size=10):
    """对图像的某个矩形区域添加马赛克"""
    roi = img[y:y + height, x:x + width]  # 提取目标区域
    # 缩小再放大，实现马赛克效果
    h, w = roi.shape[:2]
    roi_small = cv2.resize(roi, (mosaic_size, mosaic_size), interpolation=cv2.INTER_LINEAR)
    roi_mosaic = cv2.resize(roi_small, (w, h), interpolation=cv2.INTER_NEAREST)
    img[y:y + height, x:x + width] = roi_mosaic  # 将马赛克区域放回原图
    return img


# 读取视频
video_path = "/Users/huanghaoming/Documents/新闻视频工作空间/20250803001.mp4"
output_path = "/Users/huanghaoming/Documents/新闻视频工作空间/202508030011.mp4"
cap = cv2.VideoCapture(video_path)

# 获取视频信息
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 编码格式
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# 马赛克区域参数 (x, y, width, height)
mosaic_x, mosaic_y = 100, 100
mosaic_w, mosaic_h = 200, 200

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 对指定区域打马赛克
    frame = apply_mosaic(frame, mosaic_x, mosaic_y, mosaic_w, mosaic_h, mosaic_size=15)

    # 写入输出视频
    out.write(frame)

    # 显示实时效果（可选）
    cv2.imshow("Mosaic Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("视频处理完成，已保存到:", output_path)
