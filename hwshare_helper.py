# if enable yuanshen_target, then require elevated prompt
import re
import time
import os
import subprocess
import webbrowser

path = "HuaweiShare_content_share.txt"
# yuanshen = "com.miHoYo.Yuanshen.apk"
# yuanshen_target = r"C:\Program Files\Genshin Impact\Genshin Impact Game\YuanShen.exe"

while True:
    time.sleep(1)
    if os.path.exists(path):
        with open(path, "r", encoding='utf-8') as f:
            text = f.read()
            # regex to extract url
            urls = re.findall(r'(https?:\/\/[^\s]+)', text)
            print(urls)
            for url in urls:
                # open url in browse
                webbrowser.open(url)
        # delete the file
        os.remove(path)
    # if os.path.exists(yuanshen):
    #     if os.path.exists(yuanshen_target):
    #         subprocess.Popen([yuanshen_target])
    #         time.sleep(10) # wait for transmission completed 
    #         os.remove(yuanshen)
