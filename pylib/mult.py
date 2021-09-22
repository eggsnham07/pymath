#!/usr/env python3
import sys
import re

count = 0
into = 1

for arg in sys.argv:
    if not re.search("py", arg) and not re.search("mult", arg):
        into *= float(int(arg))

if isinstance(into, float):
   print(round(into))
else:
    print("One of the arguments are invalid!")
