:import requests
import os
import time

while True:
    try:
        data = requests.get(
            url='http://crm.babah24.ru/api_order/order/unhandledorders/sumid'
        )

        # if there are unhandled objects
        unhandled: bool = data.json()['unhandled']

        # apt-get install sox libsox-fmt-all
        if unhandled:
            for _ in range(6):
                os.system("ffplay -autoexit -nodisp /home/pi/Documents/NotifySoundScript/notifier.mp3")
                time.sleep(5)
        else:
            time.sleep(30)
    except Exception:
        time.sleep(10)
