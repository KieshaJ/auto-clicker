from src.clicker import Clicker
from src import constants
from src.clicker_listener import ClickerListener

thread = Clicker(constants.DELAY, constants.THREAD_DELAY, constants.BUTTON_ONE)
thread.start()

with ClickerListener(thread=thread) as listener:
    listener.join()

