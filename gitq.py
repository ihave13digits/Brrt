import json
from os import path, system
x=open(path.join("res","config.json"), "r")
y=x.read()
x.close()
z=json.loads(y)
print(z)

json_str='{"TOKEN":"","PREFIX":"'+z["PREFIX"]+'"}'
print(json_str)
x=open(path.join("res","config.json"), "w")
x.write(json_str)
x.close()



system('git commit -a -m "'+"gi"+'"')