"""
jscc quickstart
"""

"""
existing
tiny sample
Twitter Bootstrap
HTML5 Boilerplate
"""
install_type = "tiny sample"

import os
import shutil
import subprocess

def yes_or_no(msg, default="Y"):
    if default == "Y":
        yn = "[Y/n]"
    else:
        yn = "[y/N]"
    t = raw_input("%s %s> " % (msg, yn))
    if not t:
        t = default
    if t in "Yy":
        return True
    return False

def makedirs(dir):
    if os.path.isdir(dir):
        return
    os.makedirs(dir)

destination = os.path.abspath("qssample")
#use_vis_server = yes_or_no("Use visualization server?")
#use_growl = yes_or_no("Use growlnotify?")


makedirs(destination)
JSCC_PATH = os.path.join(destination, ".jscc")
makedirs(JSCC_PATH)
MAKEFILE = os.path.join(destination, "Makefile")
CLIENT_ABSPATH = os.path.abspath("client")
if os.path.isfile(MAKEFILE):
    os.rename(MAKEFILE, MAKEFILE + ".bak")

CWD = os.getcwd()
os.chdir(destination)
subprocess.call(["ln", "-s", os.path.join(CLIENT_ABSPATH, "Makefile")])
os.chdir(JSCC_PATH)
subprocess.call(["ln", "-s", os.path.join(CLIENT_ABSPATH, "build.sh")])
subprocess.call(["ln", "-s", os.path.join(CLIENT_ABSPATH, "client.py")])

