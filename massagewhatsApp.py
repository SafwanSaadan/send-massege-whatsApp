import webbrowser
import pyautogui
from time import sleep

def send(text, phone):
    webbrowser.open("whatsapp://send?text=" + text.replace('\n', '%0A') + "&phone=" + phone.replace('+', ''))
    sleep(10)
    pyautogui.click(x=1787, y=978)
    sleep(0.2)
    pyautogui.hotkey('enter')
    sleep(1)
    pyautogui.hotkey('alt', "f4")
    