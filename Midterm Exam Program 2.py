from tkinter import *
window = Tk()

window.geometry("500x300")
window.title("Midterm in OOP")

lbl = Label(window, text="Enter your fullname", fg="Red")
lbl.place(x=50, y=125)

entry1 = Entry(window,bd=2)
entry1.place(x=275, y=125)

entry2 = Entry(window, bd=2)
entry2.pack()
entry2.place(x=275, y=175)
def press():
   text = entry1.get()
   entry2.delete(0, END)
   entry2.insert(0, text)
   return

btn = Button(window, text="Click to display Fullname", fg="Red", command=press)
btn.pack()
btn.place(x=50, y=175)

window.mainloop()