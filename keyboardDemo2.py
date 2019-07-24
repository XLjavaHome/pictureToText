import keyboard
import pinyin
import pyperclip
def is_Chinese(ch):
    if '\u4e00' <= ch <= '\u9fff':
        return True
    return False
hotkey = 'ctrl+alt+p'
print(hotkey)
while True:
    if keyboard.wait(hotkey) == None:
        # 读取剪切板中的文字，并获取每个文字的首字母，复制进剪切板
        paste = pyperclip.paste()
        result = ''
        chinese = ''
        for everyOne in paste:
            if is_Chinese(everyOne):
                chinese += everyOne
                result += pinyin.get_initial(everyOne).replace(' ', '')
            else:
                # 字母的话就累加
                result += everyOne
        # 在结尾处将所有的中文都加上
        result += chinese
        pyperclip.copy(result)
        print(result)
