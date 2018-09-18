# 键盘
import os
# 截图
import time

import keyboard
import pyperclip
from PIL import ImageGrab

import baiduAPI

# 一直循环相当于while true
# for n in range(sys.maxsize):
while True:
    # 截图开始,不区分大小写
    # 加上没有用or keyboard.wait('shift+alt+a') == None
    if keyboard.wait('ctrl+alt+a') == None:
        # 截图结束 TODO 监听鼠标左键,目前只搜到python2的
        if keyboard.wait('enter') == None:
            time.sleep(0.01)
            im = ImageGrab.grabclipboard()
            picturePath = "1.png"
            if im == None:
                print("无法识别该图片")
            else:
                picturePath = os.path.join(os.getcwd(), picturePath)
                im.save(picturePath)
                # 识别图片
                result = baiduAPI.pictrueToText(picturePath)
                # 将内容复制进剪切板
                pyperclip.copy(result)
                print(result)
