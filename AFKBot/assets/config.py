import pyautogui
import secrets

def press_keys(self):
    self.SLEEP_TIME = 2
    options = {
        "keys": ['a','s','d','w',' '],
        "buttons": ['left'],
        "sleep_time": self.SLEEP_TIME * 1000
    }

    def get_random_option(options_list):
        return secrets.choice(options_list)

    def press_key(actions):
        pyautogui.press(actions)

    def click_button(click):
        pyautogui.click(button=click)

    if not self.is_running:
        return
    key = get_random_option(options["keys"])
    button = get_random_option(options["buttons"])
    press_key(key)
    click_button(button)
    self.after(options["sleep_time"], lambda: press_keys(self))

