=============================================
 JSCC: Continuous Compilation for JavaScript
=============================================

JavaScript is very loose language.
Closure Compiler helps us to keep quality of codes.

jscc does:

- watch modification of your JS files (using watchdog and goog.require dependency),
- background compile & lint (using Closure Compiler and Closure Lint),
- visualize them with dinamic graph (using Highcharts and Flask).

You can see screenshots of dinamic graphs on: https://github.com/nishio/jscc/blob/gh-pages/screenshot.png


CONTENTS
========

- client:
  client tools for continuous compilation.

- server:
  HTTP server to visualize errors and warnings.
  It also a sample usecase of JSCC.

  Makefile, build.sh, client.py are used for sample.


REQUIREMENT
===========

(*) "$ make" on top level will download several requirements.


For client
----------

- Closure Linter

  https://developers.google.com/closure/utilities/docs/linter_howto


- growlnotify

  http://growl.info/extras.php#growlnotify

  If you don't need notification with growl, uncomment it from build.sh

- Watchdog

  http://packages.python.org/watchdog/

  $ pip install watchdog


- Closure Library (*)

- Closure Compiler (*)



For server
----------

- Flask (*)

  http://flask.pocoo.org/


- Highcharts (*)

  http://www.highcharts.com/


HOW TO USE
==========

(currently we are making quickstart.py to make easy this step)
(it is obsolete, sorry)
- 1: Fork the repos on github.
- 2: 'git clone' into your project dir
- 3: Make branch: 'git checkout -b <some_name_to_identify_your_project>'
- 4: Do: jscc$ make client_install
     it does 'ln -s' jscc/client/{build.sh, Makefile, client.py}
- 5: Try 'make conftest' to configure correctly
- 6: Try 'make {deps.txt, lint, deps.js, compile}'
     especially 'make compile' fails when you set wrong LIBPATH and EXTERNS, be careful.
- 7: Run jscc/server/server.py
     It may better to use another shell not to bother with a lot of logs.
- 8: Try 'make {report, watch}'
     'make watch' also be better to run on another shell.


If you already installed jscc:

- 1: Make _jscc on your project dir
- 2: "ln -s" for build.sh, watch.py, report.py
- 3: Make Makefile (or something you want) to compile and lint your js-files. It is triggered by watch.py.



HOW TO USE WITH FLYMAKE
=======================

If you use emacs, you can highlight error/warning line on emacs.
After add *("\\.js\\'" flymake-simple-make-init)* into *flymake-allowed-file-name-masks* ,
flymake-mode call "make check-syntax" when you save files.

::

   (add-to-list 'flymake-allowed-file-name-masks
                '("\\.js\\'" flymake-simple-make-init))

   (add-hook 'java-mode-hook
             '(lambda ()
                (flymake-mode)))


HOW TO RUN SERVER ON RACKHUB
============================

- 1: Log in your rack
- 2: git clone <repos>
  (TODO: install Flask)
- 3: git checkout develop # optional
- 4: cd server
- 5: python server.py --port 3000


TODO
====

- remove watch.pid when wacter.py killed by Ctrl-C

- quickstart.py have a lot of TODO
  - make server IP and port configurable
- (done) move compile.log and lint.log into .jscc
- (done) I implemented watch.py. Use it to watch scripts' modification.
- 'server' is now a sample of jscc managed project, but in old-style.
  Make it not-jscc-managed project, and make quckstart.py can jscc-ize it.

- preserve past errors. (now just have the last data. it lost if server restarted)

- other issues

  - (done)we need nice way to kill watching process (instead of manual `kill`)
  - record what kind of error occurs, statistics?
  - be able to scroll the graph to see past
  - enbug.py will crash if empty file is passed
  - enbug.py will hung up if a whitespace-only file is passed
  - enbug.py should output bugs as line diff.
  - make graph's minimum Y == 0.
  - make graph's minimun tick >= 1


HISTORY
=======

2012-05-29 v1.1: Support Flymake
2012-03-27 First Release


THANKS
======

The jscc was developed to enhance my productivity in Cybozu Labs,
which allowed me to publish the tool. Thanks! http://labs.cybozu.co.jp/en/
