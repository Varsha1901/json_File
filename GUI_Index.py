import tkinter as tk
from tkinter import *
from tkinter import filedialog
import json

root = tk.Tk()

root.title('The game')
#You can set the geometry attribute to change the root windows size
root.geometry("1000x500") #You want the size of the app to be 500x500
root.resizable(0, 0) #Don't allow resizing in the x or y direction

#Changed variables so you don't have these set to None from .pack()

def open():
    File = filedialog.askopenfilename(parent=root,title='Choose a file')
    for f in File:
        yourName.insert(1.0, json.load(File))
    

custName = StringVar(None)
yourName = Entry(root, textvariable=custName)
yourName.grid(column=0,row=0,sticky='EW')
yourName.update()
yourName.focus_set()
yourName.place(y = 25, x = 100, width = 525, height = 25)

button = Button(root, text='Browse',command = open)
button.place( x = 650, y = 25)

close = tk.Button(text='Quit', command=root.destroy)
close.pack()

root.mainloop()
