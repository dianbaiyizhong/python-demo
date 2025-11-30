import requests
import os
from urllib.parse import unquote


def download_nba_team_images():
    # NBA球队图片链接列表
    team_urls = [
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Atlanta-Hawks-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Boston-Celtics-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Brooklyn-Nets-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Charlotte-Hornets-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Chicago-Bulls-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Cleveland-Cavaliers-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Dallas-Mavericks-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Denver-Nuggets-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Detroit-Pistons-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Golden-State-Warriors-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Houston-Rockets-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Indiana-Pacers-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/LA-Clippers-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Los-Angeles-Lakers-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Memphis-Grizzlies-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Miami-Heat-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Milwaukee-Bucks-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Minnesota-Timberwolves-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/New-Orleans-Pelicans-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/New-York-Knicks-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Oklahoma-City-Thunder-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Orlando-Magic-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Philadelphia-76ers-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Phoenix-Suns-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Portland-Trail-Blazers-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Sacramento-Kings-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/San-Antonio-Spurs-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Toronto-Raptors-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Utah-Jazz-wallpaper-logo-desktop-NBA-2025-2026.png",
        "https://www.prosportsbackgrounds.com/wp-content/uploads/Washington-Wizards-wallpaper-logo-desktop-NBA-2025-2026.png"
    ]

    # 创建保存图片的文件夹
    save_dir = "nba_team_images"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    successful_downloads = 0
    failed_downloads = []

    for url in team_urls:
        try:
            # 从URL中提取球队名称
            # 格式: .../Team-Name-wallpaper-logo-desktop-NBA-2025-2026.png
            filename = url.split('/')[-1]  # 获取文件名部分
            team_part = filename.split('-wallpaper')[0]  # 获取球队名称部分

            # 处理特殊球队名称
            if team_part == "LA":
                team_name = "clippers"
            elif team_part == "Los-Angeles":
                team_name = "lakers"
            else:
                # 提取最后一个单词作为球队名（小写）
                team_name = team_part.split('-')[-1].lower()

            # 构建保存路径
            save_path = os.path.join(save_dir, f"{team_name}.png")

            print(f"正在下载: {team_part} -> {team_name}.png")

            # 发送请求下载图片
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()  # 如果请求失败会抛出异常

            # 保存图片
            with open(save_path, 'wb') as f:
                f.write(response.content)

            print(f"✓ 成功下载: {team_name}.png")
            successful_downloads += 1

        except Exception as e:
            error_msg = f"✗ 下载失败: {url} - 错误: {str(e)}"
            print(error_msg)
            failed_downloads.append((url, str(e)))

    # 输出下载总结
    print(f"\n=== 下载总结 ===")
    print(f"成功下载: {successful_downloads} 张图片")
    print(f"失败: {len(failed_downloads)} 张图片")

    if failed_downloads:
        print("\n失败的下载:")
        for url, error in failed_downloads:
            print(f"  {url} - {error}")


def main():
    print("开始下载NBA球队图片...")
    download_nba_team_images()
    print("\n下载完成！图片保存在 'nba_team_images' 文件夹中")


if __name__ == "__main__":
    main()
