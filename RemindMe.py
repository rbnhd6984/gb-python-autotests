import json
import sched
import time
import multiprocessing
import ctypes
from datetime import datetime

# Функция для отображения тултипа
def show_tooltip(message):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, message, 'Напоминание!', 0x40 | 0x1)

# Функция напоминания
def reminder(reminder_data):
    scheduler = sched.scheduler(time.time, time.sleep)
    now = datetime.now()

    for reminder in reminder_data:
        remind_time = datetime.strptime(reminder["время_напоминания"], '%d.%m.%Y %H:%M')
        if now < remind_time:
            delay = (remind_time - now).total_seconds()
            scheduler.enter(delay, 1, show_tooltip, argument=(reminder["сообщение"],))
    scheduler.run()

# Функция для сохранения напоминаний в JSON файл
def save_reminder_to_json(message, remind_time):
    try:
        with open('reminders.json', 'r', encoding='utf-8') as file:
            reminders = json.load(file)
    except FileNotFoundError:
        reminders = []

    reminder_data = {
        "сообщение": message,
        "время напоминания": remind_time.strftime('%d.%m.%Y %H:%M')
    }
    reminders.append(reminder_data)
    
    with open('reminders.json', 'w', encoding='utf-8') as file:
        json.dump(reminders, file, ensure_ascii=False, indent=4)

# Загрузка всех напоминаний из файла
def load_reminders():
    try:
        with open('reminders.json', 'r', encoding='utf-8') as file:
            reminders = json.load(file)
    except FileNotFoundError:
        reminders = []
    return reminders

# Основная логика программы
if __name__ == "__main__":
    # Загрузка и запуск всех напоминаний
    reminders = load_reminders()
    if reminders:
        reminder_process = multiprocessing.Process(target=reminder, args=(reminders,))
        reminder_process.start()
        print("Все напоминания загружены и запущены. Программа работает в фоне...")

# Возможность добавления новых напоминаний
while True:
    action = input("Хотите добавить новое напоминание? (да/нет): ")
    if action.lower() == 'да':
        message = input("Введите сообщение для напоминания: ")
        remind_time_str = input("Введите дату и время для напоминания (ДД.ММ.ГГГГ ЧЧ:ММ): ")
        remind_time = datetime.strptime(remind_time_str, '%d.%m.%Y %H:%M')
        save_reminder_to_json(message, remind_time)
        # Перезапуск процесса напоминаний с обновленным списком
        reminders = load_reminders()
        if reminder_process.is_alive():
            reminder_process.terminate()
        reminder_process = multiprocessing.Process(target=reminder, args=(reminders,))
        reminder_process.start()
        print("Новое напоминание добавлено и запущено.")
    else:
        break
