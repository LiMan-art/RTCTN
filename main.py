import calendar, tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time

def mess_info():
    
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo('ЭЭЭЭЭЭЭЭЙ', 'ПРОВЕРЬ ОПОВЕЩЕНИЕ') # текст уведомления(заголовок, текст)

def data_info():

    mont = datetime.now()

    day = int(mont.strftime('%d'))
    monday = int(mont.strftime('%m'))
    year = int(mont.strftime('%Y'))
    hour = int(mont.strftime('%H'))


    ymd = calendar.weekday(year, monday,day)

    return ymd, hour


def warning():

    last = None

    while True:

        ymd,hour = data_info()
        key = (datetime.now().strftime('%Y-%m-%d'), hour)

        if hour == 00: # полночь, любой день
            if key != last:
                mess_info()
                last = key

        elif ymd == 5 or ymd == 6: # выходные
            if hour == 12: # полдень
                if key != last:
                    mess_info()
                    last = key

        time.sleep(60)

if __name__ == '__main__':

    warning()


