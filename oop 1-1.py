from tkinter import *
window = Tk()

window.geometry("400x300")
window.title("Welcome to Python Programming")

#Button Widget

btn = Button(window, text = "Click to add", fg = "Blue")
btn.place(x = 50, y = 120)

#Label Widget

lbl = Label(window, text = "Student Personal Information", fg = "Blue", bg = "Light Blue")
lbl.place(relx = .5, rely = 0.2, anchor = "center")

lbl2 = Label(window, text = "Gender", fg = "Blue", bg = "Light Blue")
lbl2.place(x = 50, y = 150)

lbl3 = Label(window, text = "Sports", fg = "Blue", bg = "Light Blue")
lbl3.place(x = 50, y = 210)

lbl4 = Label(window, text = "Subjects:", fg = "Blue", bg = "Light Blue")
lbl4.place(x = 50, y = 255)

#Text Field Widget

txtfld = Entry(window, bd = 2, font = ("Bebas Neue", 12))
txtfld.place(x = 140, y = 120)

#Radio Button

v1 = StringVar()
v2 = StringVar()
v1.set(1)
rd1 = Radiobutton(window, text = "Male", value = v1)
rd1.place(x = 50, y = 170)

r2 = Radiobutton(window, text = "Female", value = v2)
r2.place(x = 50, y = 190)

#CheckBox Widget

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
chkbx = Checkbutton(window, text = "Basketball", variable = v3)
chkbx2 = Checkbutton(window, text = "Tennis", variable = v4)
chkbx3 = Checkbutton(window, text = "Swimming", variable =v5)

chkbx.place(relx = .25, y = 230)
chkbx2.place(relx = .5, y = 230)
chkbx3.place(relx = .7, y = 230)

#ListBox Widget

var = StringVar()
var.set("Student 1")
data1 = "Arithmetic"
data2 = "Reading"
data3 = "Writing"
lstbx = Listbox(window, height = 5, selectmode = "multiple")
lstbx.insert(END, data1, data2, data3)
lstbx.place(x = 50, y = 280)

window.mainloop()