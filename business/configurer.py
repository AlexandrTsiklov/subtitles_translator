import requests, json, pytesseract, cv2

from config.usersettings import *


# Subtitles properties

FONT = cv2.FONT_HERSHEY_COMPLEX
LINE_TYPE = cv2.LINE_AA

def calc_amount_chars_per_line():
    teststring = ''
    for i in range(1000):
        textsize, _ = cv2.getTextSize(teststring, cv2.FONT_HERSHEY_COMPLEX, FONT_SCALE, FONT_THICKNESS)
        if textsize[0] >= SCREEN_WIDTH * LINE_WIDTH_LIMIT:
            break
        else:
            teststring += 's'
    return len(teststring)

MAX_CHARACTERS_PER_LINE = calc_amount_chars_per_line()


# Pytesseract properties

pytesseract.pytesseract.tesseract_cmd = r'C:\<YOUR PATH TO TESSERACT>\tesseract.exe'



# Yandex translator properties

def update_iamtoken():
    response = requests.post(URL_FOR_IAM_TOKEN, json=DATA_FOR_IAM_TOKEN)
    return json.loads(response.text).get('iamToken') if response.status_code == 200 else ''

QAUTH_TOKEN: str = '<YOUR QAUTH TOKEN>'
URL_FOR_IAM_TOKEN = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
DATA_FOR_IAM_TOKEN = {'yandexPassportOauthToken': '{}'.format(QAUTH_TOKEN)}
IAM_TOKEN: str = update_iamtoken()
FOLDER_ID: str = '<YOUR FOLDER ID>'


# Notion properties

NOTION_TOKEN = 'YOUR NOTION TOKEN'
NOTION_HEADERS = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}