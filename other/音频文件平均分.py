from pydub import AudioSegment
import os


def split_audio_evenly(file_path, n_parts, output_dir='output'):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 加载音频文件
    audio = AudioSegment.from_file(file_path)

    # 获取总时长（毫秒）
    total_duration = len(audio)

    # 计算每段的长度
    part_duration = total_duration // n_parts

    # 分割音频
    for i in range(n_parts):
        start_time = i * part_duration
        end_time = (i + 1) * part_duration if i < n_parts - 1 else total_duration

        # 提取片段
        part = audio[start_time:end_time]

        # 保存片段
        output_file = os.path.join(output_dir, f'part_{i + 1}.mp3')
        part.export(output_file, format="mp3")
        print(f"Exported {output_file}")


if __name__ == "__main__":
    input_file = "/Users/huanghaoming/Downloads/CleanShot/CleanShot 2025-01-12 at 14.41.17.mp3"  # 替换为你的音频文件路径
    number_of_parts = 2  # 将音频文件平均切割成5份
    split_audio_evenly(input_file, number_of_parts)
