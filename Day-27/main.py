from tkinter import *
#creating window:
window = Tk()
window.minsize(width = 300 , height = 100)
window.title("Miles to km convertor")

def convert():
    val = (float)(b1.get())
    newVal = val*1.60934
    l3.config(text=str(newVal)+" km")
#logic:

l1 = Label(text="is equal to")
l1.place(x=30,y=50)
l1.config(padx=20,pady=20)
b1 = Entry()
b1.place(x=50,y=30)

l2 = Label(text="Miles")
l2.place(x=150,y=15)
l2.config(padx=20,pady=20)

l3 = Label(text="0")
l3.place(x=120,y=70)

b = Button(text="Convert",command=convert)
b.place(y=90,x=130)
#running the window:
window.mainloop()
