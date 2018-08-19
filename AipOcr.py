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

image = get_file_content('1.png')

""" 调用通用文字识别, 图片参数为本地图片 """
print(client.basicGeneral(image))

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image, options)

url = "https//www.x.com/sample.jpg"

""" 调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url, options)
