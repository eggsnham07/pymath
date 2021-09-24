#!/usr/env python3
import sys
import re

count = 0
into = 0

for arg in sys.argv:
    if not re.search("py", arg) and not re.search("add", arg):
        try:
            into += arg
        except:
            print("[ERROR]: Argument must be an integer/float!")
            exit(1)
            

if isinstance(into, int):
   print(round(float(int(into))))
else:
    print("One of the arguments are invalid!")
