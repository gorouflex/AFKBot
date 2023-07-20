# Config
import pyautogui
import random

# Your sleep time goes here (seconds)
SLEEP_TIME = 3

class KeyPresser:
    def __init__(self):
        self.SLEEP_TIME = SLEEP_TIME
        self.options = {
            # This is the list of key the bot will pressing
            "keys": ['a', 's', 'd', 'w', ' '],
            # This is the way the bot will press the mouse, only have 2 option: 'left' and 'right'
            "buttons": ['left'],
            "sleep_time": self.SLEEP_TIME * 1000
        }
        self.is_running = True

    def press_keys(self):
        if not self.is_running:
            return
        key = random.choice(self.options["keys"])
        button = random.choice(self.options["buttons"])
        pyautogui.press(key)
        pyautogui.click(button=button)
        pyautogui.sleep(self.SLEEP_TIME)
        self.press_keys()
