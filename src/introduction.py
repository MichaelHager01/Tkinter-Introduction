# Michael Hager

from tkinter import *
from tkinter import messagebox

root1 = Tk()
root1.title("Fridge Count")

# Creating Frame
root = LabelFrame(root1, padx=20, pady=20)
root.pack(padx=20, pady=20)

i = 7
inventory = []

# Functions
def add(inventory):
    item = __add.get()
    for obj in inventory:
        if item == obj:
            messagebox.showerror("ERROR", "Item is already in fridge")
            __add.delete(0, END)
            return
    if (len(item) > 0):
        inventory.append(item)
        __add.delete(0, END)
    return

def take(inventory):
    item = __take.get()
    found = False
    for j in range(len(inventory)):
        if (item == inventory[j]):
            inventory.pop(j)
            found = True
    if not(found):
        messagebox.showerror("ERROR", "Item is not found in fridge")
    __take.delete(0, END)
    return

def inv(inventory):
    global i
    _sp4 = Label(root, text=" ")
    _sub = Label(root, text="Inventory: ")
    _sp4.grid(row=i)
    i += 1
    _sub.grid(row=i, column=0)
    for k in inventory:
        _listing = Label(root, text=k)
        _listing.grid(row=i, column=1)
        i += 1
    i += 1
    return


# Defining GUI
_s1 = Label(root, text=" ")
_s2 = Label(root, text=" ")
_s3 = Label(root, text=" ")

_title = Label(root, text="Welcome to your Fridge!", font="Arial", bg="#A7C7E7")

_add = Label(root, text="Add: ", font="Arial")
_take = Label(root, text="Take out: ", font="Arial")

__add = Entry(root)
__take = Entry(root)

_enter1 = Button(root, text="Enter", borderwidth=3, font="Arial", command=lambda: add(inventory))
_enter2 = Button(root, text="Enter", borderwidth=3, font="Arial", command=lambda: take(inventory))
_enter3 = Button(root, text="Check Inventory", width=18, borderwidth=3, command=lambda: inv(inventory))


# Formatting GUI
_s1.grid(row=0)
_title.grid(row=1, column=1)
_s2.grid(row=2)

_add.grid(row=3, column=0)
_take.grid(row=4, column=0)

__add.grid(row=3, column=1, columnspan=2)
__take.grid(row=4, column=1, columnspan=2)

_enter1.grid(row=3, column=3)
_enter2.grid(row=4, column=3)
_s3.grid(row=5)
_enter3.grid(row=6, column=1, columnspan=2)


root.mainloop()

