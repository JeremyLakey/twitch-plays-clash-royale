import pyautogui
import time

def get_mouse_location():
    while True:
        print(pyautogui.position())
        time.sleep(2)




if __name__ == "__main__":
    get_mouse_location()
