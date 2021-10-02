import pyautogui
import pyperclip
import time

def doTyping(text):
    time.sleep(3)
    pyautogui.write(text)


if __name__ == '__main__':
    text = ""
    while True:
        time.sleep(2)
        if text==pyperclip.paste():
            pass
        else:
            text = pyperclip.paste()
            doTyping(text)
