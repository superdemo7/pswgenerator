from threading import Thread
from time import sleep
import os
import signal
def clear():
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 
def restart():
    global time_left
    time_left = default_time
def countdown():
    global time_left, running
    while running:
        time_left -= 1
        sleep(1)
        if time_left == 0:
            break    
    if running:
        clear()
        print('Se ha cerrado sesion por seguridad')
        os.kill(os.getpid(),signal.SIGINT)
def stop():
    global running
    running = False
def pause():
    global time_left
    time_left = -1

running = True
default_time = 180
time_left = default_time
timer_thread = Thread(target=countdown)
timer_thread.start()