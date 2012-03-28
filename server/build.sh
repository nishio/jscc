# assure only one script run on one time
lockfile -r 0 build.lock || exit 1
growlnotify -m "begin CI"

#
# Run Compiler
#
make compile

#
# Run Lint
#
make lint

#
# Report
#
make report

growlnotify -m "end CI"
rm -f build.lock