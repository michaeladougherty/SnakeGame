from tkinter import *
from tkinter import ttk

#This is the grid for the game
def play_screen(win):
    row_count = 0
    for i in range(0, 12, 2):
        for x in range(12):
            if row_count%2 == 0:
                if x % 2 == 1:
                    ttk.Separator(
                        master=win,
                        orient=HORIZONTAL,
                        style='even.TSeparator',
                        class_=ttk.Separator,
                        takefocus=1,
                        cursor='plus'
                    ).grid(row=i, column=x, sticky="nsew",pady=0, padx=0)
                else:
                    ttk.Separator(
                        master=win,
                        orient=HORIZONTAL,
                        style='odd.TSeparator',
                        class_=ttk.Separator,
                        takefocus=1,
                        cursor='plus'
                    ).grid(row=i, column=x, sticky="nsew",pady=0, padx=0)

        for i in range(1, 12, 2):
            for x in range(12):
                if row_count % 2 == 0:
                    if x % 2 == 1:
                        ttk.Separator(
                            master=win,
                            orient=HORIZONTAL,
                            style='odd.TSeparator',
                            class_=ttk.Separator,
                            takefocus=1,
                            cursor='plus'
                        ).grid(row=i, column=x, sticky="nsew",pady=0, padx=0)
                    else:
                        ttk.Separator(
                            master=win,
                            orient=HORIZONTAL,
                            style='even.TSeparator',
                            class_=ttk.Separator,
                            takefocus=1,
                            cursor='plus'
                        ).grid(row=i, column=x, sticky="nsew", pady=0, padx=0)