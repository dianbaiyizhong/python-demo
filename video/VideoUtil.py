import cv2
import numpy as np


def mask_bottom_right_corner(frame, corner_size=0.25):
    """
    将给定帧的右下角部分设置为黑色。

    :param frame: 输入的视频帧 (numpy.ndarray)
    :param corner_size: 右下角部分相对于整个帧的比例，默认为 0.25 (25%)
    :return: 修改后的帧 (numpy.ndarray)
    """
    height, width = frame.shape[:2]

    # 计算右下角区域的尺寸
    corner_height = 30
    corner_width = int(width * corner_size)



    # 设置右下角区域为黑色
    frame[height - corner_height:, width - corner_width:] = [0, 0, 0]

    return frame


def process_video(input_path, output_path, corner_size=0.25):
    """
    处理输入视频文件，将每帧的右下角部分设置为黑色，并保存结果到输出文件。

    :param input_path: 输入视频文件路径
    :param output_path: 输出视频文件路径
    :param corner_size: 右下角部分相对于整个帧的比例，默认为 0.25 (25%)
    """
    # 打开输入视频文件
    cap = cv2.VideoCapture(input_path)

    # 获取视频属性
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 定义编码器并创建 VideoWriter 对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用 mp4 编码
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 修改帧
        modified_frame = mask_bottom_right_corner(frame, corner_size)

        # 写入修改后的帧到输出文件
        out.write(modified_frame)

        # 显示处理进度（可选）
        cv2.imshow('Processing', modified_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 清理资源
    cap.release()
    out.release()
    cv2.destroyAllWindows()
