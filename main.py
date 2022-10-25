from tkinter import *
from tkinter import ttk
import snakeScreen
import Title
import tkinter.font as font
import math

# Creating Window for Viewing
window = Tk()
window.configure(bg="#86b357")
#  Set name of window
window.title("Snake Game")
#  Set size of the window
window.geometry("500x500")
window.resizable(False, False)

# Creating a style for the grid of lines
styl = ttk.Style()
styl.configure("even.TSeparator", background='light grey')
styl.configure("odd.TSeparator", background='grey')

# Creating the collums and grid system to hold the elements of the window
for i in range(12):
    window.rowconfigure(i, weight=1)

for i in range(12):
    window.columnconfigure(i, weight=1)




# Code is going to go under this

Title.title_screen(window)



# Keeping the program running
window.mainloop()