#!/usr/env python3
import sys
import re

count = 0
into = 0
intt = 0

for arg in sys.argv:
    if not re.search("py", arg):
        if count == 0:
            into = float(int(arg))
            count += 1
        elif count == 1:
            intt = float(int(arg))
            count += 1

if isinstance(into, float) and isinstance(intt, float):
   print(round(into * intt))
else:
    print("One of the arguments are invalid!")
