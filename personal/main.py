import requests
import time
import datetime
import logging

n = 0
file_log = logging.FileHandler('Log.log')
console_out = logging.StreamHandler()

# print(r.content)  # если хотим ответ в байтах

while True:
    n = n + 1
    result = requests.get("https://okzadapter2-mortgageloan.dev.akbars.ru/health")
    # print(n, ":", str(datetime.datetime.strftime(datetime.datetime.now(), '%Y.%m.%d %H:%M:%S')), str(result.text))
    logging.basicConfig(handlers=(file_log, console_out),
                        format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S',
                        level=logging.INFO)

    logging.info(result.text)

    time.sleep(2)
