import webview
import pyperclip
from keyboard import is_pressed
from pyautogui import press,hotkey
from time import sleep


class APP:
    is_running = False
    def start(self,Message,Where,Hotkey):
        self.is_running = True
        pyperclip.copy(Message)
        while True:
            sleep(0.2)
            if self.is_running == True and is_pressed(Hotkey) and Where == 'all':
                press('y')
                sleep(0.1)
                hotkey('ctrl','v')
                sleep(0.1)
                press('enter')
            elif self.is_running == True and is_pressed(Hotkey) and Where == 'team':
                press('u')
                sleep(0.1)
                hotkey('ctrl','v')
                sleep(0.1)
                press('enter')
            else:
                pass


    def stop(self):
        pyperclip.copy('')
        self.is_running = False

if __name__ == "__main__":
    app = APP()
    webview.create_window('CS2 Chat Spammer v1.0.0',url='src/index.html',js_api=app,width=330,height=410,resizable=False)
    webview.start()