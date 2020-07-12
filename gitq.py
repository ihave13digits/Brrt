import json
from os import path, system
import sys
x=open(path.join("res","config.json"), "r")
y=x.read()
x.close()
z=json.loads(y)
print(z)

json_str='{"TOKEN":"1","PREFIX":"'+z["PREFIX"]+'"}'
print(json_str)
x=open(path.join("res","config.json"), "w")
x.write(json_str)
x.close()


commit_message = ""
for x in sys.argv:
    if not x == "gitq.py":
        commit_message = commit_message + " " + x


print(commit_message)
system('git commit -a -m "'+commit_message+'"')

json_str='{"TOKEN":'+z["TOKEN"]+',"PREFIX":"'+z["PREFIX"]+'"}'
print(json_str)
x=open(path.join("res","config.json"), "w")
x.write(json_str)
x.close()