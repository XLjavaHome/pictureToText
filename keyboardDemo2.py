import keyboard
import pinyin
import pyperclip
def is_Chinese(ch):
    if '\u4e00' <= ch <= '\u9fff':
        return True
    return False
while True:
    if keyboard.wait('ctrl+alt+p') == None:
        # 读取剪切板中的文字，并获取每个文字的首字母，复制进剪切板
        paste = pyperclip.paste()
        # 以字母开头不用复制
        if is_Chinese(paste[0]):
            result = pinyin.get_initial(paste).replace(' ', '')
            pyperclip.copy(result + paste)
            print(result)
