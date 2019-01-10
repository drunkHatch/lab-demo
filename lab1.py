#!/usr/bin/env python3
import requests as req

print(req.__version__)

r = req.get("http://google.com/")
#print(r.text)

my_py = req.get("https://github.com/drunkHatch/lab-demo.git")
print(my_py.text)
