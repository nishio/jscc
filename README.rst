=============================================
 JSCC: Continuous Compilation for JavaScript
=============================================

JavaScript is very loose language.
Closure Compiler helps us to keep quality of codes.

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


- Watchdog

  http://packages.python.org/watchdog/

  $ pip install watchdog


- Closure Library (*)

- Closure Compiler (*)



For server
----------

- Flask

  http://flask.pocoo.org/


- Highcharts (*)

  http://www.highcharts.com/


HOW TO USE
==========

- 1: Fork the repos on github.
- 2: 'git clone' into your project dir
- 3: 'git checkout -b <some_name_to_identify_your_project>'
- 4: 'ln -s' jscc/client/{build.sh, Makefile, client.py}
- 5: try 'make {deps.txt, lint, deps.js, compile}'
- 6: run jscc/server/server.py
- 7: try 'make {report, watch}'


ISSUES
======

- we need nice way to kill watching process
- enbug.py will crash if empty file is passed
- enbug.py will hung up if a whitespace-only file is passed
- enbug.py should output bugs as line diff.
- when you clone jscc in your working dir
  and set 'LIBPATH = .', a namespace 'main.main' provided in jscc/server/static/main.js
  may conflict other 'main.main' in your scripts.
