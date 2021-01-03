from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time


class myHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)


folder_to_track = "/home/work/Downloads/tracking_folder"
folder_destination = "/home/work/Downloads/destination_folder"
event_handler = myHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
