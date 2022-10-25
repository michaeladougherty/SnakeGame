from tkinter import *

import snakeScreen

def callback():
    global buttonClicked
    buttonClicked = not buttonClicked

buttonClicked  = False

def title_screen(win):
    play_button = Button(win, text="Normal", bg= "#37612a", fg= "#c7d63e" ,command=lambda: [snakeScreen.play_screen(win)])
    play_button.grid(column=0,columnspan= 6, row= 10, rowspan= 11, sticky= "NESW")

    inf_play_button = Button(win, text="Infinite", bg= "#37612a", fg= "#c7d63e", command=lambda: [snakeScreen.play_screen(win)])
    inf_play_button.grid(column=6, columnspan=12, row=10, rowspan=11, sticky= "NESW")

