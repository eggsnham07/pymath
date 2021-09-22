#!/usr/bin/env python3
import tkinter as tk
import os, re, math, sys
from pathlib import Path

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.init_gui()

    def init_gui(self):
        self.output = tk.Entry(self.master)
        self.output.place(x=0,
                y = 0,
                width = 240,
                height = 30)
        self.output.configure(state='disabled')

        self.calc = tk.Button(self.master)
        self.calc["text"] = "Calculate"
        self.calc["command"] = lambda:self.exec(self.en.get())
        self.calc.pack(side="bottom")

        self.en = tk.Entry(self.master, width=240)
        self.en.pack(side="bottom")

    def outp(self, string):
        self.output.configure(state='normal')
        self.output.delete(0, "end")
        self.output.insert(0, str(string))
        self.output.configure(state="disabled")

    def exec(self, string):
        args = string.split(" ")
        equ = 0
        if re.search("add", args[0]):
            print("Addition mode")
            for s in args:
                if not re.search("add", s):
                    if re.search(".", s): s = float(s)
                    else: s = float(int(s))
                    if isinstance(s, float):
                        equ += s
            print(equ)
            self.outp(equ)

        elif re.search("mult", args[0]):
            print("Multiply mode")
            count = 1
            for s in args:
                if not re.search("mult", s):
                    if re.search(".", s): s = float(s)
                    else: s = float(int(s))
                    if isinstance(s, float):
                        if count == 1:
                            count += 1
                            equ = 1
                        equ *= s
            print(equ)
            self.outp(equ) 

        elif re.search("sub", args[0]):
            print("Subtraction mode")
            count = 1
            for s in args:
                if not re.search("sub", s):
                    if re.search(".", s): s = float(s)
                    else: s = float(int(s))
                    if isinstance(s, float):
                        if count == 1:
                            count += 1
                            equ = s
                        else:
                            equ -= s
            print(equ)
            self.outp(equ) 

        elif re.search("div", args[0]):
            print("Division mode")
            count = 1
            for s in args:
                if not re.search("div", s):
                    if re.search(".", s): s = float(s)
                    else: s = float(int(s))
                    if isinstance(s, float):
                        if count == 1:
                            count += 1
                            equ = s
                        else:
                            equ /= s

            print(equ)
            self.outp(equ)
        
        elif re.search("sqr", args[0]):
            print("Square root mode")
            if re.search(".", args[1]): s = float(args[1])
            else: s = float(int(args[1]))
            equ = math.sqrt(s)

            print(equ)
            self.outp(equ)

arg_len = 0

for arg in sys.argv:
    arg_len += 1

if arg_len == 2 and sys.argv[arg_len-1] == "gui":
    root = tk.Tk()
    root.geometry("240x100")
    app = App(master=root)
    app.mainloop()
else:
    print("Invalid arguments!")
