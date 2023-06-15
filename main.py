from src.clicker import Clicker
from src.clicker_listener import ClickerListener

thread = Clicker()
thread.start()

with ClickerListener(thread=thread) as listener:
    listener.join()

