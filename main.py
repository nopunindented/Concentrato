import sys
import time
import subprocess
from subprocess import check_output
from threading import Timer
from GUIfile import *


class StudyFocusConcentratApp(Ui_Form):
    def __init__(self, Form):
        self.setupUi(Form)

        self.pushButton.clicked.connect(self.get_study_time)
        self.pushButton_2.clicked.connect(self.according_to_the_breaktime)
        self.pushButton_3.clicked.connect(self.run_program)
        self.pushButton_4.clicked.connect(self.stop_program)

    def check_if_program_running(self):
        global processname
        processname = ['Discord.exe', 'Spotify.exe']
        tasks_running = check_output('tasklist')
        for i in range(0, len(processname)):
            if processname[i] in str(tasks_running):
                subprocess.call(["taskkill", "/F", "/IM", processname[i]])
                print('{} has been closed'.format(processname[i]))
            else:
                setattr

    def get_study_time(self):
        study_periods = int(self.plainTextEdit.text())
        global end_of_study_periodt
        end_of_study_periodt = time.time() + study_periods

    def according_to_the_breaktime(self):
        global break_time_is
        break_time_is = int(self.plainTextEdit_2.text())

    def run_program(self):
        studying = True
        global still_studying
        still_studying = True
        while studying:
            while time.time() < end_of_study_periodt:
                self.check_if_program_running()
            time.sleep(break_time_is)

    def stop_program(self):
        quit()


"""
study_period = int(
    input("How long is the study period? Please enter a time: "))
break_time = int(
    input("How long do you want your break to be? Please enter a time: "))


def close_program(program):
    subprocess.call(["taskkill", "/F", "/IM", program])


def end_check():
    return None


def check_if_programs_running():
    global processname
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
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.exec_()
