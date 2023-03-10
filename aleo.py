import requests
import re
import time
from datetime import datetime
from bs4 import BeautifulSoup

COINBASE_MIN = 1
INCENTIVES_MIN = 0.01
SOLUTIONS_MIN = 2
SLEEP_TIME_SEC = 360

API_TOKEN = "2109:AA-LL_EEOO"
CHAT_ID = "-1703"
ADDRESSES = {
    "num1-serv1": "aleo...address1",
    "num2-serv2": "aleo...address2",

    
}

def send_tg_msg(value: str):

    try:

        requests.post(

            f"https://api.telegram.org/bot{API_TOKEN}/sendMessage",

            json={

                'chat_id': CHAT_ID,

                'text': value

            }

        )

    except Exception as e:

        print(e.args)
