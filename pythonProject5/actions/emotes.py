import pyautogui
import time

last_emote_time: float = time.time()


def maybe_emote(content):
    global last_emote_time
    if (time.time() - last_emote_time) > 3:
        if content == "emote 1":
            emote_1()
            last_emote_time = time.time()
            return True

        elif content == "emote 2":
            emote_2()
            last_emote_time = time.time()
            return True

        elif content == "emote 3":
            emote_3()
            last_emote_time = time.time()
            return True

        elif content == "emote 4":
            emote_4()
            last_emote_time = time.time()
            return True

        elif content == "emote 5":
            emote_5()
            last_emote_time = time.time()
            return True

        elif content == "emote 6":
            emote_6()
            last_emote_time = time.time()
            return True

        elif content == "emote 7":
            emote_7()
            last_emote_time = time.time()
            return True

        elif content == "emote 8":
            emote_8()
            last_emote_time = time.time()
            return True

# emote button
# Point(x=706, y=895)

# emote 1
# Point(x=801, y=717)
def emote_1():
    pyautogui.click(706,895)
    pyautogui.click(801,717)
    pyautogui.moveTo(100,100)


# emote 2
# Point(x=906, y=720)
def emote_2():
    pyautogui.click(706,895)
    pyautogui.click(906,717)
    pyautogui.moveTo(100,100)

# emote 3
# Point(x=1006, y=723)
def emote_3():
    pyautogui.click(706,895)
    pyautogui.click(1006,717)
    pyautogui.moveTo(100,100)

# emote 4
# Point(x=1112, y=722)
def emote_4():
    pyautogui.click(706,895)
    pyautogui.click(1112,717)
    pyautogui.moveTo(100,100)

# emote 5
# Point(x=799, y=805)
def emote_5():
    pyautogui.click(706,895)
    pyautogui.click(799,805)
    pyautogui.moveTo(100,100)

# emote 6
# Point(x=901, y=809)
def emote_6():
    pyautogui.click(706,895)
    pyautogui.click(901,809)
    pyautogui.moveTo(100,100)

# emote 7
# Point(x=1005, y=810)
def emote_7():
    pyautogui.click(706,895)
    pyautogui.click(1005,810)
    pyautogui.moveTo(100,100)

# emote 8
# Point(x=1111, y=805)
def emote_8():
    pyautogui.click(706,895)
    pyautogui.click(1111,805)
    pyautogui.moveTo(100,100)