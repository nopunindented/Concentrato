import time
import subprocess
from subprocess import check_output
from threading import Timer


study_period = int(
    input("How long is the study period? Please enter a time: "))
break_time = int(
    input("How long do you want your break to be? Please enter a time: "))


def close_program(program):
    subprocess.call(["taskkill", "/F", "/IM", program])


def end_check():
    return None


def check_if_programs_running():
    global processnamefc
    processname = ['Discord.exe', 'Spotify.exe']
    tasks_running = check_output('tasklist')
    for i in range(0, len(processname)):
        if processname[i] in str(tasks_running):
            close_program(processname[i])
            print('{} has been closed'.format(processname[i]))
        else:
            setattr


def study_break_time():
    time.sleep(break_time)


def according_to_break_time():
    studying = True
    global still_studying
    still_studying = True
    while studying:
        end_of_study_period = time.time() + study_period
        while time.time() < end_of_study_period:
            check_if_programs_running()
        time.sleep(break_time)


if __name__ == "__main__":
    according_to_break_time()
