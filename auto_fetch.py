import requests
import os
from datetime import datetime

def fetch_and_save():
    url = "https://ua.fongmi.eu.org/box.php?url=http://fty.xxooo.cf/tv"
    try:
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        # 文件名：年月日_时分秒.txt
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(resp.text)
        print(f"✅ 已保存：{filename}")
    except Exception as e:
        print(f"❌ 失败：{e}")

if __name__ == "__main__":
    fetch_and_save()
