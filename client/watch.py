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
import argparse

# for watchdog version
from time import sleep
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
import atexit

MTIME = False  # use deps.txt and mtime polling to check modification
# read files in deps.txt
# check mtime
# tentative version
if 0:
    DEPS_FILE_NAME = 'deps.txt'

    files_mtime = {}
    deps_mtime = os.path.getmtime(DEPS_FILE_NAME)
    for filename in file(DEPS_FILE_NAME):
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


# TODO: BUILD_COMMAND is now build.sh on same directory of the file. Take them from args.
BUILD_COMMAND = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'build.sh')

PID_FILE = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'watch.pid')

to_build = False  # flag by what watch thread notify to build thread

def write_own_pid():
    # if pid-file exists, warn and exit
    if os.path.isfile(PID_FILE):
        print 'watch.pid exists. Watch process is already running?'
        sys.exit(1)

    # write own pid
    pid = os.getpid()
    fo = file(PID_FILE, 'w')
    fo.write(str(pid))
    fo.close()


def build():
    "run build.sh async"
    subprocess.call([BUILD_COMMAND], shell=True)


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        filename = os.path.split(event.src_path)[1]
        if not filename.endswith('.js'): return
        if filename.endswith('_flymake.js'): return
        global to_build
        to_build = True


def start_watchdog_observer():
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=args.jsdir, recursive=True)
    observer.schedule(event_handler, path=args.externdir, recursive=True)
    observer.start()

    @atexit.register
    def _exit():
        observer.stop()
        observer.join()


def start_mainloop():
    global to_build
    while True:
        if to_build:
            to_build = False
            build()
        sleep(1)


def remove_pid():
    print 'removing pid file:', PID_FILE
    os.remove(PID_FILE)


def kill():
    if os.path.isfile(PID_FILE):
        pid = file(PID_FILE).read()
        print 'killing', pid
        subprocess.call(['kill', pid], shell=True)
        remove_pid()


def main():
    global args
    parser = argparse.ArgumentParser(description='Watch js-files modifications.')
    parser.add_argument('--kill', dest='kill', action='store_true',
                        help='kill watching process')
    parser.add_argument('--jsdir', dest='jsdir',
                        help='where js files to observe are placed')
    parser.add_argument('--externdir', dest='externdir',
                        help='where extern files to observe are placed')

    args = parser.parse_args()
    if args.kill:
        kill()
    else:
        write_own_pid()
        build()
        start_watchdog_observer()
        try:
            start_mainloop()
        except:
            import traceback
            traceback.print_exc()
            remove_pid()

if __name__ == '__main__':
    main()
