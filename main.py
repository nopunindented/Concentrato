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


def check_if_programs_running():
    global processname
    processname = ['Discord.exe', 'Spotify.exe']
    tasks_running = check_output('tasklist')
    for i in range(0, len(processname)):
        if processname[i] in str(tasks_running):
            close_program(processname[i])
            print('{} has been closed'.format(processname[i]))
        else:
            print('Not found')


def according_to_break_time(study):
    studying = True
    while studying:
        check_if_programs_running()


if __name__ == "__main__":
