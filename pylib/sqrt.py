#!/usr/bin/env python3
import sys, re, math

final = 0

for arg in sys.argv:
    if not re.search("py", arg) and not re.search("sq", arg):
        try:
            final = math.sqrt(float(int(arg)))
        except:
            print("[ERROR]: Argument must be an integer/float!")
            exit(1)

print(final)
