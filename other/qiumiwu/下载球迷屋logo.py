logos = 'ATL, BOS, BKN, CHA, CHI, CLE, DAL, DEN, DET, GSW, HOU, IND, LAC, LAL, MEM, MIA, MIL, MIN, NOP, NYK, OKC, ORL, PHI, PHX, POR, SAC, SAS, TOR, UTA, WAS'
import requests

teams = '''qiumiwu_Hawks,  
qiumiwu_Celtics,  
qiumiwu_Nets,  
qiumiwu_Hornets,  
qiumiwu_Bulls,  
qiumiwu_Cavaliers,  
qiumiwu_Mavericks,  
qiumiwu_Nuggets,  
qiumiwu_Pistons,  
qiumiwu_Warriors,  
qiumiwu_Rockets,  
qiumiwu_Pacers,  
qiumiwu_Clippers,  
qiumiwu_Lakers,  
qiumiwu_Grizzlies,  
qiumiwu_Heat,  
qiumiwu_Bucks,  
qiumiwu_Timberwolves,  
qiumiwu_Pelicans,  
qiumiwu_Knicks,  
qiumiwu_Thunder,  
qiumiwu_Magic,  
qiumiwu_76ers,  
qiumiwu_Suns,  
qiumiwu_Blazers,  
qiumiwu_Kings,  
qiumiwu_Spurs,  
qiumiwu_Raptors,  
qiumiwu_Jazz,  
qiumiwu_Wizards'''

arr = logos.split(", ")
arr1 = teams.split(",  \n")

print(arr1)
for index, e in enumerate(arr):
    pass
    url = ("https://file.qiumiwu.com/team/" + e + "_300.png")
    save_path = arr1[index].lower() + ".png"  # 保存路径和文件名
    print(save_path)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功

        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # 过滤保持活跃状态的新块
                    f.write(chunk)
        print(f"文件已保存到 {save_path}")

    except Exception as e:
        print(f"下载失败: {e}")
