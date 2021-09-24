#!/usr/bin/env python3
import math, sys, re

class Math:
    def add(argv):
        count = 0
        into = 0

        for arg in argv: into += float(int(arg))

        if isinstance(into, float):
            print(round(float(int(into))))
        else:
            print("One of the arguments are invalid!")
    def sub(argv):
        into = 0
        count = 0

        for arg in argv:
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

    def div(argv):
        count = 0
        into = 0
        intt = 0

        for arg in argv:
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

    def mult(argv):
        count = 0
        into = 1

        for arg in argv:
            try:
                into *= float(int(arg))
            except:
                print("[ERROR]: Argument must be an integer/float!")
                exit(1)

        if isinstance(into, float):
            print(round(into))
        else:
            print("One of the arguments are invalid!")

    def sqrt(argv):
        try:
            final = math.sqrt(float(int(argv)))
        except:
            print("[ERROR]: Argument must be an integer/float!")
            exit(1)
        print(final)

args = sys.argv
nums = []

if re.search("add", args[1]):
    for arg in args:
        if not re.search("add", arg) and not re.search("py", arg):
            try:
                nums.append(float(int(arg)))        
            except:
                print(f"[ERROR]: Invalid Integer/Float: '{arg}'")
                exit(1)
    print(Math.add(nums))
    nums = []
elif re.search("sub", args[1]):
    for arg in args:
        if not re.search("sub", arg) and not re.search("py", arg):
            try:
                nums.append(float(int(arg)))
            except:
                print(f"[ERROR]: Invalid Integer/Float: {arg}")
                exit(1)
    print(Math.sub(nums))
    nums = []
elif re.search("div", args[1]):
    for arg in args:
        if not re.search("div", arg) and not re.search("py", arg):
            try:
                nums.append(float(int(arg)))
            except:
                print(f"[ERROR]: Invalid Integer/Float: {arg}")
                exit(1)
    print(Math.div(nums))
    nums = []
elif re.search("mult", args[1]):
    for arg in args:
        if not re.search("mult", arg) and not re.search("py", arg):
            try:
                nums.append(float(int(arg)))
            except:
                print(f"[ERROR]: Invalid Integer/Float: {arg}")
    print(Math.mult(nums))
    nums = []
elif re.search("sqr", args[1]):
    for arg in args:
        if not re.search("sqr", arg) and not re.search("py", arg):
            try:
                print(Math.sqrt(float(int(arg))))
            except:
                print(f"[ERROR]: Invalid Integer/Float: {arg}")
                exit(1)