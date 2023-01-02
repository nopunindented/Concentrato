import sys
import time
import subprocess
from subprocess import check_output
from threading import Timer
from tkinter import *
import threading

"""
study_period = int(
    input("How long is the study period? Please enter a time: "))
break_time = int(
    input("How long do you want your break to be? Please enter a time: "))
"""


def close_program(program):
    subprocess.call(["taskkill", "/F", "/IM", program])


def end_check():
    return None


def check_if_programs_running():
    global processname
    processname = ['Discord.exe', 'Spotify.exe',
                   'Steam.exe', 'EpicGamesLauncher.exe']
    tasks_running = check_output('tasklist')
    for i in range(0, len(processname)):
        if processname[i] in str(tasks_running):
            close_program(processname[i])
            print('{} has been closed'.format(processname[i]))
        else:
            setattr


studying = True


window = Tk()
window.geometry("600x200")


name = Entry(window, width=20, font=('Arial 18'))
name.pack(padx=10, pady=10)

names = Entry(window, width=20, font=('Arial 18'))
names.pack(padx=10, pady=10)


def start():
    global studying
    studying = True
    global study_period
    study_period = name.get()
    global break_time
    break_time = names.get()


def according_to_break_time():
    global still_studying
    still_studying = True
    while studying:
        end_of_study_period = time.time() + int(name.get())
        while time.time() < end_of_study_period:
            check_if_programs_running()
            window.update()
        print("break time")
        window.update()
        time.sleep(int(names.get()))
    window.update()


def stop():
    global studying
    studying = False
    window.destroy()
    exit()


start = Button(window, text="Start", font="Arial, 12",
               command=threading.Thread(target=start()).start).pack()
end = Button(window, text="Stop", font="Arial, 12", command=stop).pack()

window.after(20000, according_to_break_time)
window.mainloop()
