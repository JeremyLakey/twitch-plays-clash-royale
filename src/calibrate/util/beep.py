from sys import platform

if platform == "win32":
    import winsound

frequency = 1000
duration = 100


def beep():
    if platform == "win32":
        winsound.Beep(frequency, duration)
    else:
        print("\a")