#!/usr/bin/env python3
import sys
import re

count = 0
into = 0
intt = 0

for arg in sys.argv:
    if not re.search(".py", arg) and not re.search("0", arg):
        if count == 0:
            into = arg
            count += 1
        elif count == 1:
            intt = arg
            count += 1
print(int(into) * int(intt))
