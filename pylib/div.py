#!/usr/env python3
import sys
import re

count = 0
into = 0
intt = 0

for arg in sys.argv:
   if not re.search("py", arg) and not re.search("div", arg):
      try:
         if count == 0:
               into = float(int(arg))
               count += 1
         elif count == 1:
               intt = float(int(arg))
               count += 1
      except:
            print("[ERROR]: Argument must be an integer/float!")
            exit(1)

if isinstance(into, float) and isinstance(intt, float):
   print(round(into / intt))
else:
    print("One of the arguments are invalid!")
