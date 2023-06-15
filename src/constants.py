from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode

DELAY = 3
THREAD_DELAY = 1
MOUSE = Controller()
BUTTON_ONE = Button.left
START_KEY = KeyCode(char="z")
STOP_KEY = KeyCode(char="x")
THREAD_STOP_KEY = KeyCode(char="c")
CLICKER_TAG = "----- [AC] ----- "
START_TEXT = CLICKER_TAG + "Clicker started..."
STOP_TEXT = CLICKER_TAG + "Clicker stopped..."
THREAD_STOP_TEXT = CLICKER_TAG + "Thread stopped. Exiting program"

