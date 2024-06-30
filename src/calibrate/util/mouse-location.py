import pyautogui
import time
from calibrate.util.beep import beep

def get_mouse_location():
    while True:
        print(pyautogui.position())
        beep()
        time.sleep(2)




if __name__ == "__main__":
    get_mouse_location()
