import time 
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="t")
clicking = False
mouse = Controller()

def clicker():
    #perform a click if clicking variable is set to true
    while True:
        if clicking:
            mouse.click(Button.left,1)
        #sleep so theres enough time to activate or deactivate
        time.sleep(0.001)

def toggle_event(key):
    if key == TOGGLE_KEY:
        #change state of clicking
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

#listen for key presses
with Listener(on_press=toggle_event) as listener:
    listener.join()