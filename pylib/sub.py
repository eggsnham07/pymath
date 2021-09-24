#!/usr/bin/env python3
import re
import sys

into = 0
count = 0

for arg in sys.argv:
    if not re.search("py", arg) and not re.search("sub", arg):
        try:
            if count == 0:
                into = float(int(arg))
                count += 1
            else:
                into -= float(int(arg))
        except:
            print("[ERROR]: Argument must be an integer/float!")
            exit(1) 

if isinstance(into, float):
   print(round(into))
else:
    print("One of the arguments are invalid")
