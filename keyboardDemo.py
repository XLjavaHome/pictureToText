# 键盘
import sys
# 截图
import time

import keyboard
import pyperclip
from PIL import ImageGrab

import baiduAPI

for n in range(sys.maxsize):
    # 截图开始,不区分大小写
    if keyboard.wait('Ctrl+alt+a') == None:
        # 截图结束 TODO 监听鼠标左键,目前只搜到python2的
        if keyboard.wait('enter') == None:
            time.sleep(0.01)
            im = ImageGrab.grabclipboard()
            picturePath = "1.png"
            if im == None:
                print("无法识别该图片")
            else:
                im.save(picturePath)
                # 识别图片
                result = baiduAPI.pictrueToText(picturePath)
                # 将内容复制进剪切板
                pyperclip.copy(result)
                print(result)
                print('内容在剪切板中')
