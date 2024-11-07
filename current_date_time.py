# Программа выводящая текущие дату и время каждые 10 сек

import time
from datetime import datetime

# Функция для вывода текущей даты и времени
def print_current_time():
    while True:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%d.%m.%Y %H:%M:%S")
        print(formatted_time)
        time.sleep(10)

print_current_time()