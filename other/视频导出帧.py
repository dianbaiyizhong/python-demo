import cv2
import os


def extract_frames_opencv(video_path, output_dir, frame_interval=1):
    """
    使用OpenCV提取视频帧

    Args:
        video_path: 视频文件路径
        output_dir: 输出目录
        frame_interval: 帧间隔，默认为1（提取每一帧）
    """
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("无法打开视频文件")
        return

    # 获取视频信息
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    print(f"视频信息: {total_frames}帧, {fps:.2f}FPS, 时长: {duration:.2f}秒")

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # 按间隔保存帧
        if frame_count % frame_interval == 0:
            # 生成文件名
            filename = f"frame_{saved_count:06d}.jpg"
            filepath = os.path.join(output_dir, filename)

            # 保存帧
            cv2.imwrite(filepath, frame)
            saved_count += 1

            if saved_count % 100 == 0:
                print(f"已保存 {saved_count} 帧...")

        frame_count += 1

    cap.release()
    print(f"完成！共保存 {saved_count} 帧到 {output_dir}")


# 使用示例
if __name__ == "__main__":
    video_path = "/Users/huanghaoming/Downloads/nba2k16_raw.mp4"  # 替换为你的视频路径
    output_dir = "../extracted_frames"

    extract_frames_opencv(video_path, output_dir, frame_interval=1)
