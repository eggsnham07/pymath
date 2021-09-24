#!/usr/bin/env python3
import math

class Math:
    def add(argv):
        count = 0
        into = 0

        for arg in argv:
            try:
                into += arg
            except:
                print("[ERROR]: Argument must be an integer/float!")
                exit(1)
                    

        if isinstance(into, int):
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