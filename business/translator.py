import requests
import json

from configurer import *
from notiontool import *


class Language:
    Russian = 'ru'
    English = 'en'


def build_request(text, source_language, target_language):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(IAM_TOKEN)
    }
    body = {
        "targetLanguageCode": target_language,
        "texts": text,
        "folderId": FOLDER_ID,
    }
    return headers, body


def send_request(body, headers):
    return requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate', json=body, headers=headers)


def parse_response(response):
    data = json.loads(response.text)
    return data['translations'][0]['text']


def translate(native_text, src_lang, trg_lang):
    headers, body = build_request(native_text, src_lang, trg_lang)
    response = send_request(body, headers)
    target_text = parse_response(response)
    NotionConnector.activetext = native_text + ' - ' + target_text
    return target_text