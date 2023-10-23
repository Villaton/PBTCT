import tkinter as tk
from threading import Thread
import time
import beep

stop_countdown = False

def countdown(seconds):
    global stop_countdown
    while seconds:
        if stop_countdown:
            stop_countdown = False
            return
        time.sleep(1)
        seconds -= 1
        beep.play_seconds_voice(seconds)
        if seconds < 10:
            beep.play_beep_short()
        # Add graphical field to show seconds
        seconds_label.config(text=f"Seconds remaining: {seconds}")
    beep.play_beep_long()

def start_timer():
    global seconds
    seconds = int(entry.get())
    Thread(target=countdown, args=(seconds,)).start()

def stop_timer():
    global stop_countdown
    stop_countdown = True

root = tk.Tk()

start_button = tk.Button(root, text='Start', command=start_timer, width=10, height=3)
start_button.pack(side=tk.LEFT)

stop_button = tk.Button(root, text='Stop', command=stop_timer, width=10, height=3)
stop_button.pack(side=tk.RIGHT)

entry = tk.Entry(root)
entry.pack()

seconds_label = tk.Label(root, text="", font=("Arial", 30))
seconds_label.pack()

root.mainloop()

