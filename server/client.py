import re
import json
from datetime import datetime
import urllib2
import urllib

data = {"error": None, "warning": None}
messages = []
for line in open("lint.log"):
    if line.startswith("Line"):
        # sample: Line 58, E:0002: Missing space after ","
        messages.append(line.split(":", 2)[1])

data["lint"] = len(messages)


success = False
for line in open("compile.log"):
    if "error(s)" in line or "warning(s)" in line:
        # sample: 44 error(s), 0 warning(s)
        err, warn = re.match("(\d+) error.* (\d+) warn", line).groups()
        data["error"] = int(err)
        data["warning"] = int(warn)
    if "closurebuilder.py: JavaScript compilation succeeded" in line:
        success = True
        if data["error"] == None: data["error"] = 0
        if data["warning"] == None: data["warning"] = 0


data["when"] = datetime.now().isoformat()
data["success"] = success
urllib2.urlopen("http://localhost:8104/api/put?" + urllib.urlencode({"json": json.dumps(data)}))

