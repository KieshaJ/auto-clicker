from pynput.keyboard import Listener

from src import constants

class ClickerListener(Listener):
    def __init__(self, thread):
        super(ClickerListener, self).__init__(on_press=self.on_press)
        self.thread = thread

    def on_press(self, key):
        if key == constants.START_KEY and not self.thread.running:
            print(constants.START_TEXT)
            self.thread.start_clicks()
        elif key == constants.STOP_KEY and self.thread.running:
            print(constants.STOP_TEXT)
            self.thread.stop_clicks()
        elif key == constants.THREAD_STOP_KEY:
            print(constants.THREAD_STOP_TEXT)
            self.thread.exit()
            self.stop()

