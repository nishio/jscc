"""
watch modification of files in deps.txt

In initial version, I use watchmedo:
cat deps.txt | xargs watchmedo shell-command --command="./build.sh" &

However I want to control some feature

- kill "watch" process by "make stop-watch"
- when deps.txt changed, chenge targets of watch
"""

import os
import sys
import subprocess

DEPS_FILE_NAME = "deps.txt"
BUILD_COMMAND = "./build.sh"

# if pid-file exists, warn and exit
if os.path.isfile("watch.pid"):
    print "watch.pid exists. Watch process is already running?"
    sys.exit(1)

# write own pid
pid = os.getpid()
fo = file("watch.pid", "w")
fo.write(str(pid))
fo.close()

# run build.sh async
def build():
    subprocess.call([BUILD_COMMAND], shell=True)

build()




# read files in deps.txt
# check mtime
if 0:
    files_mtime = {}
    deps_mtime = os.path.getmtime(DEPS_FILE_NAME)
    for filename in file("deps.txt"):
        filename = filename.strip()
        mtime = os.path.getmtime(filename)
        files_mtime[filename] = mtime

    print deps_mtime, files_mtime

    #
    # wait and check again

    # if deps.txt modified since last time, run build.sh
    mtime = os.path.getmtime(DEPS_FILE_NAME)
    if mtime != deps_mtime:
        build()
        deps_mtime = mtime
    else:
        pass


from time import sleep
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
import atexit

import logging
logging.basicConfig(level='INFO')

to_build = False
class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        filename = os.path.split(event.src_path)[1]
        if not filename.endswith(".js"): return
        if filename.endswith("_flymake.js"): return
        global to_build
        to_build = True

if __name__ == "__main__":
    event_handler = MyHandler()
    #event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path='../js', recursive=True)
    observer.start()

    @atexit.register
    def _exit():
        observer.stop()
        observer.join()

    while True:
        if to_build:
            to_build = False
            build()
        sleep(1)



