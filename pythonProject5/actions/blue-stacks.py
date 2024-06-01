import pyautogui

showing_blue_stack_controls = True


def is_showing_controls():
    global showing_blue_stack_controls
    return showing_blue_stack_controls


def toggle_controls_hints():
    global showing_blue_stack_controls
    pyautogui.hotkey('ctrl', 'shift', 'f6')
    showing_blue_stack_controls = not showing_blue_stack_controls

