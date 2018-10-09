import keyboard
import pinyin
import pyperclip
while True:
    if keyboard.wait('ctrl+alt+p') == None:
        # 读取剪切板中的文字，并获取每个文字的首字母，复制进剪切板
        paste = pyperclip.paste()
        result = pinyin.get_initial(paste).replace(' ', '')
        pyperclip.copy(result)
        # print(result)
