# hwshare_helper
This project is a small tool for handling url-containing texts delivered by HUAWEI Share on Windows.

## config
Before use, please install Python. Place hwshare_helper.py in the Huawei Share folder where all files received by Huawei Share are placed.

## usage
You may run hwshare_helper.py in the background by run the following script in Huawei Share folder in the terminal.
```
pythonw.exe hwshare_helper
```
By default, it automatically acquire the text delivered by Huawei Share, and open the url inside it. **Then the text will be deleted**. The purpose of this script is to enable consistent experience among HUAWEI share between PC, tablets and phones.
