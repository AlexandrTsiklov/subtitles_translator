import requests, json

from configurer import *


def get_listdata(text):
    return json.dumps({
        "children": [
            {
                "object": "block",
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": text
                            }
                        }
                    ]
                }
            }
        ]
    })

class NotionUrls:
    newC1_url = 'https://api.notion.com/v1/blocks/<ID OF YOUR PAGE>/children'


class NotionConnector:
    activetext = ''

    @staticmethod
    def send_to_list(url):
        if NotionConnector.activetext:
            requests.patch(url, headers=NOTION_HEADERS, data=get_listdata(NotionConnector.activetext))