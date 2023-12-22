from time import sleep

import pyautogui


def action(x: float, y: float):
    """
    Moves mouse from one point to the other (3s duration).
    Presses alt at the end.
    """
    pyautogui.moveTo(x, y, duration=3)
    pyautogui.press("alt")


def main_loop(sleep_time: int = 10):
    """
    Performs action until interrupted, with 'sleep_time'
    sleep periods in between.
    """
    x, y = pyautogui.size()

    print("Autoactive running, press CTRL-C to exit.")
    try:
        while True:
            action(x * 0.1, y * 0.1)
            sleep(sleep_time * 60)
            action(x * 0.9, y * 0.9)
            sleep(sleep_time * 60)

    except KeyboardInterrupt:
        print("\nExiting.")
