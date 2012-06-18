"""
jscc quickstart
"""
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


JSCC_ROOT = os.path.abspath(os.path.dirname(__file__))
CWD = os.getcwd()
if JSCC_ROOT != CWD:
    # TODO: FIXME
    raise NotImplementedError("now you need to run this in %s" % JSCC_ROOT)

# TODO: changable
destination = os.path.abspath("qssample")
# TODO: ask them
#use_vis_server = yes_or_no("Use visualization server?")
#use_growl = yes_or_no("Use growlnotify?")

# TODO: choose from them
"""
existing
tiny sample
Twitter Bootstrap
HTML5 Boilerplate
"""
install_type = "tiny sample"


makedirs(destination)
JSCC_PATH = os.path.join(destination, ".jscc")
makedirs(JSCC_PATH)
CLIENT_ABSPATH = os.path.abspath("client")

NEW_MAKEFILE = os.path.join(destination, "Makefile")
# if exists, make backup
if os.path.isfile(NEW_MAKEFILE):
    os.rename(NEW_MAKEFILE, NEW_MAKEFILE + ".bak")

# make sure to have depends files
subprocess.call(["make"])
# TODO: changable, these are defalut value
CLOSURE_LIB_PATH = os.path.abspath("client/thirdparty/closure-library")
CLOSURE_COMPILER_PATH = os.path.abspath("client/thirdparty/compiler.jar")

# make Makefile
data = open("client/MakefileTemplate").read()
VARIABLES = dict(
    CLOSURE_LIB_PATH=CLOSURE_LIB_PATH,
    CLOSURE_COMPILER_PATH=CLOSURE_COMPILER_PATH,
)
data = data.format(**VARIABLES)
data = open(NEW_MAKEFILE, "w").write(data)


os.chdir(destination)
if install_type == "tiny sample":
    SAMPLE_DIR = os.path.join(JSCC_ROOT, "client", "sample", "tiny")
    shutil.copy(os.path.join(SAMPLE_DIR, "index.html"), ".")
    makedirs("js")
    shutil.copy(os.path.join(SAMPLE_DIR, "main.js"), "js")
    os.chdir(os.path.join(destination, "js"))
    subprocess.call(["ln", "-s", CLOSURE_LIB_PATH])

os.chdir(JSCC_PATH)
subprocess.call(["ln", "-s", os.path.join(CLIENT_ABSPATH, "build.sh")])
subprocess.call(["ln", "-s", os.path.join(CLIENT_ABSPATH, "client.py")])
subprocess.call(["ln", "-s", os.path.join(CLIENT_ABSPATH, "watch.py")])
