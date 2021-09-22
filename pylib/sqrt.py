#!/usr/bin/env python3
import sys, re, math

final = 0

for arg in sys.argv:
    if not re.search("py", arg) and not re.search("sq", arg):
        final = math.sqrt(float(int(arg)))

print(final)
