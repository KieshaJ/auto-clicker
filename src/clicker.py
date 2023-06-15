import time
import threading

from src import constants

class Clicker(threading.Thread):
    def __init__(self):
        super(Clicker, self).__init__();
        self.mouse = constants.MOUSE
        self.delay = constants.DELAY
        self.thread_delay = constants.THREAD_DELAY
        self.button = constants.BUTTON_ONE
        self.running = False
        self.thread_running = True

    def start_clicks(self):
        self.running = True

    def stop_clicks(self):
        self.running = False

    def exit(self):
        self.stop_clicks()
        self.thread_running = False

    def run(self):
        while self.thread_running:
            while self.running:
                self.mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(self.thread_delay)

