import tkinter as tk
import time
import datetime
import threading
import socket
import subprocess

socket.setdefaulttimeout(10)

win = tk.Tk()
win.title('Alarm Clock')
win.geometry('200x50')

var = tk.StringVar()

fm = tk.Frame(win)
label = tk.Label(fm, textvariable=var, justify='left')
label.pack(side='bottom', anchor='w')

fm.pack(side='left', padx=10)


def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.daemon = True
    t.start()


def loop_clock():
    while True:
        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        hour_now = date_now.hour
        min_now = date_now.minute
        sec_now = date_now.second
        print(hour_now, min_now, sec_now)
        if hour_now == 7 and min_now == 00 and sec_now == 00:
            subprocess.Popen(["open", "-n", "https://www.youtube.com/watch?v=coYw-eVU0Ks"])
        var.set(date_str)
        time.sleep(1)


thread_it(loop_clock)
win.mainloop()
