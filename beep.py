import os
import time
from pygame import mixer

def play_beep_short():
    mixer.init()
    mixer.music.load('beep_short_1.wav')
    mixer.music.play()

def play_beep_long():
    mixer.init()
    mixer.music.load('beep_long_1.wav')
    mixer.music.play()

def countdown_beep(seconds):
    while seconds:
        time.sleep(1)
        seconds -= 1
        if seconds < 10:
            play_beep_short()
    play_beep_long()

def play_seconds_voice(seconds):
    mixer.init()
    if seconds == 10:
        mixer.music.load('10_seconds.mp3')
        mixer.music.play()
    elif seconds == 30:
        mixer.music.load('30_seconds.mp3')
        mixer.music.play()
    elif seconds == 60:
        mixer.music.load('One_minute.mp3')
        mixer.music.play()