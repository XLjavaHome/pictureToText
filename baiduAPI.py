from aip import AipOcr
""" 你的 APPID AK SK """
APP_ID = '11695638'
API_KEY = 'MFO5aHQ4IL37Q5ghIiSSnRZ0'
SECRET_KEY = 'LOUz72LeeLGb9Y8kt2F64jRVibEtQrIY'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    # r读 b二进制
    with open(filePath, 'rb') as fp:
        return fp.read()
def pictrueToText(pictruePath):
    image = get_file_content(pictruePath)
    """ 调用通用文字识别, 图片参数为本地图片 """
    texts = client.basicGeneral(image)
    # 字典和列表
    allText = []
    for word in texts['words_result']:
        text = word.get('words', '')
        # 去掉两端空格
        # 如果allText等于空 前面不要加\n
        if text.strip() != '':
            allText.append(text);
    return "\n".join(allText)
