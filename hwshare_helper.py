import re
import time
import os
import subprocess
import webbrowser
import pyperclip
from io import BytesIO
import win32clipboard
from PIL import Image
folder_path = """C:\Huawei Share\Huawei Share"""
text_path = r"C:\Huawei Share\Huawei Share\HuaweiShare_content_share.txt"


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

# yuanshen = "com.miHoYo.Yuanshen.apk"
# yuanshen_target = r"C:\Program Files\Genshin Impact\Genshin Impact Game\YuanShen.exe"
files = os.listdir(folder_path)
jpg_files = [_ for _ in files if _[-4:] == ".jpg"]
png_files = [_ for _ in files if _[-4:] == ".png"]

while True:
    time.sleep(1)
    files = os.listdir(folder_path)
    jpg_files_new = [_ for _ in files if _[-4:] == ".jpg"]
    png_files_new = [_ for _ in files if _[-4:] == ".png"]
    print(jpg_files_new)
    print(jpg_files)
    # compare and find all new photos in the folder
    jpg_files_diff = [_ for _ in jpg_files_new if _ not in jpg_files]
    png_files_diff = [_ for _ in png_files_new if _ not in png_files]
 
    for jpg_file in jpg_files_diff:            
        filepath = folder_path + "\\" + jpg_file
        print(filepath)
        image = Image.open(filepath)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        send_to_clipboard(win32clipboard.CF_DIB, data)
        time.sleep(1)
    for png_file in png_files_diff:
        filepath = folder_path + "\\" + png_file
        print(filepath)
        image = Image.open(filepath)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        send_to_clipboard(win32clipboard.CF_DIB, data)
        time.sleep(1)

    jpg_files = jpg_files_new
    png_files = png_files_new

    if os.path.exists(text_path):
        with open(text_path, "r", encoding='utf-8') as f:
            text = f.read()
            # regex to extract url
            urls = re.findall(r'(https?:\/\/[^\s]+)', text)
            print(urls)
            if len(urls) > 0:
                for url in urls:
                    # open url in browse
                    webbrowser.open(url)
            else:
                # if no urls found, copy text to clipboard
                pyperclip.copy(text)
        # delete the file
        os.remove(text_path)
  #  if os.text_path.exists(yuanshen):
   #     if os.text_path.exists(yuanshen_target):
    #        subprocess.Popen([yuanshen_target])
     #       time.sleep(10) # wait for transmission completed 
      #      os.remove(yuanshen)


