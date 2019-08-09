#!/usr/local/bin/python3
# encoding: utf-8

from tkinter import *
from tkinter import ttk

entryform_visible = 0


class mainWindow:
    def __init__(self, master):
        self.master = master
        master.title("AppTittle")
        master.minsize(width=700, height=200)           

        def show_entryform():
            global entryform_visible
            if entryform_visible == 1:
                hide_entryform()
                return
            else:
                entryform_visible = 1
                # Form for data entry (bottom of main window)
                status_txt.set("Introducing new data...")
                self.bottomframe.pack(side=BOTTOM, fill=X)

        def hide_entryform(): 
            global entryform_visible
            self.bottomframe.pack_forget()
            entryform_visible = 0
            status_txt.set("Introduction of data was cancelled.")

        def add_register():
            hide_entryform()
            status_txt.set("New register added!")                  

        # Tool bar (buttons)
        self.topframe = ttk.Frame(root, padding="3 3 12 12")
        self.topframe.pack(side=TOP, fill=X)
        btn_add = ttk.Button(self.topframe, text="Button1").pack(side=LEFT)
        btn_add = ttk.Button(self.topframe, text="+", width=2, command=show_entryform).pack(side=RIGHT)
        btn_add = ttk.Button(self.topframe, text="Button2").pack(side=RIGHT)

        # Data table (center area of window)
        self.mainframe = ttk.Frame(root)
        self.mainframe.pack(side=TOP, fill=X)

        tree = ttk.Treeview(self.mainframe, height=25, selectmode='extended')
        tree['columns'] = ('id', 'name', 'descr')
        tree.pack(side=TOP, fill=BOTH)
        tree.column('#0', anchor=W, minwidth=0, stretch=0, width=0)
        tree.column('id', anchor=W, minwidth=30, stretch=0, width=40)
        tree.column('name', minwidth=30, stretch=1, width=30)
        tree.column('descr', minwidth=100, stretch=1, width=200)
        tree.heading('id', text="ID")
        tree.heading('name', text="Name")
        tree.heading('descr', text="Description")

        # Data entry form
        self.bottomframe = ttk.Frame(root, padding="3 3 12 12")
        ttk.Label(self.bottomframe, text="Field 1").pack(side=LEFT)
        text_input_obj = ttk.Entry(self.bottomframe, width=13)
        text_input_obj.pack(side=LEFT)
        text_input_obj.focus_set()
        btn_add = ttk.Button(self.bottomframe, text="Add", command=add_register).pack(side=RIGHT)
        # We are going to pack() this later (when the user clicks the '+' button)

        # Status bar
        self.statusframe = ttk.Frame(root, padding="2 2 2 2")
        self.statusframe.pack(side=BOTTOM, fill=X)
        status_txt = StringVar()
        self.statusbar = ttk.Label(self.statusframe, textvariable=status_txt).pack(side=LEFT)


root = Tk()
appwindow = mainWindow(root)
root.mainloop()
