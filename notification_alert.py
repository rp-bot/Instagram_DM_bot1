import pyperclip
import time
import re
import pyautogui as pt
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as keyboard_con
import library as lib


def linetag():
    newlogfile_users = open(lib.logfile_users, "a")
    newlogfile_chatnum = open(lib.logfile_chatnum, 'a')
    firstline_eval_u = open(f"{lib.logfile_users}", 'r').readlines()
    firstline_eval_c = open(f"{lib.logfile_chatnum}", 'r').readlines()
    if len(firstline_eval_u) == 0:
        print('hey from 0lines')
        newlogfile_users.write(f"--/{lib.tdy}")
    else:
        newlogfile_users.write(f"\n\n--/{lib.tdy}")

    if len(firstline_eval_c) == 0:
        print('hey from 0lines')
        newlogfile_chatnum.write(f"--/{lib.tdy}")
    else:
        newlogfile_chatnum.write(f"\n\n--/{lib.tdy}")


def logger(username="", chatnum="", u=False, c=False):
    fu = open(f"{lib.logfile_users}", 'a')
    fc = open(f"{lib.logfile_chatnum}", 'a')
    if u is True:
        fu.write(f"\n{lib.now} - //@{username} sent a new msg")
    elif c is True:
        fc.write(f"\n{lib.now} - ({chatnum}) new messages")
    fu.close()
    fc.close()


def copy():
    keyboard = keyboard_con()
    keyboard.press(Key.ctrl)
    time.sleep(1)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')


def logusernames(numofchats):
    for num in range(numofchats):
        pyperclip.copy('')
        y = 345 + (num * 70)
        pt.moveTo(265, y, duration=0.5)
        pt.leftClick(duration=.3)
        pt.moveTo(948, 207, duration=0.3)
        pt.leftClick(duration=0.2)
        pt.moveTo(639, 367, duration=.7)
        pt.tripleClick(interval=0.4)
        copy()
        searchusername = re.search(r".*(?= won't)", pyperclip.paste()).group()
        logger(username=searchusername, u=True)
        if num == 0:
            logger(chatnum=numofchats, c=True)
        elif num > 0:
            pass
        pt.moveTo(824, 158, duration=0.3)
        pt.leftClick(duration=0.2)


def getstatus():
    pyperclip.copy('')
    howmanychats_loc = (1118, 290)
    mouse = Controller()
    mouse.position = howmanychats_loc
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(0.4)
    mouse.click(Button.left, 1)
    copy()
    time.sleep(1.1)
    mouse.move(200, 0)
    time.sleep(.5)
    mouse.click(Button.left, 1)


def checkstatus():
    global chatnum
    chatnum = 0
    while chatnum < 1:
        time.sleep(1)
        getstatus()
        time.sleep(1)
        status = re.search(r'(?<=\()\w+(?=\))', pyperclip.paste())
        if status:
            chatnum = int(status.group())
            linetag()
            logusernames(chatnum)
            break
        else:
            continue
