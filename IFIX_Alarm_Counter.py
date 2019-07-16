from tkinter import *
import sys


#Creates the GUI
root = Tk()

Title = root.title("CEMA Code Builder")
#This makes it a fix size
root.geometry('500x500')

rows = 0

while rows < 50:
    root.rowconfigure(rows, weight = 1)
    root.columnconfigure(rows, weight = 1)
    rows += 1


################################################################################################
# runs the actual program
################################################################################################

root.mainloop()
