import sys
import time
import os
import datetime

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class AutoTest(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def process(self, event):
        os.system('nosetests tests')

        print(datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p"))

    def on_modified(self, event):
        self.process(event)


if __name__ == '__main__':
    path = '.'
    observer = Observer()
    observer.schedule(AutoTest(), path=path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
