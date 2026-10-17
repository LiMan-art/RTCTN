import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
from ProdCalendar import ProdCalendar

calendar = ProdCalendar(cache_dir='.cache/')


def mess_info():
    
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo('ЭЭЭЭЭЭЭЭЙ', 'ПРОВЕРЬ ОПОВЕЩЕНИЕ') # текст уведомления(заголовок, текст)

def data_info():

    mont = datetime.now()

    hour = int(mont.strftime('%H'))

    return hour


def warning():

    last = None

    while True:
        now = datetime.now()
        is_day_off = not calendar.isWorkDay(now.date())
        hour = data_info()
        key = (datetime.now().strftime('%Y-%m-%d'), hour)

        if hour == 00: # полночь, любой день
            if key != last:
                mess_info()
                last = key

        elif is_day_off and hour == 12: # выходные и праздник(полдень)
            if key != last:
                mess_info()
                last = key

        time.sleep(60)

if __name__ == '__main__':

    warning()


