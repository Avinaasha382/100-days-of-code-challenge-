from tkinter import *
#creating window:
window = Tk()
window.minsize(width = 300 , height = 100)
window.title("Miles to km convertor")
window.config(padx=20,pady=20)
def convert():
    val = (float)(mileVal.get())
    newVal = val*1.60934
    outPut.config(text=str(newVal)+" km")
#logic:

mileVal = Entry()
mileVal.grid(column=1,row=0)

mileLabel = Label(text="Miles")
mileLabel.grid(column=2,row=0)

isEqlLabel = Label(text="is equal to")
isEqlLabel.grid(column=0,row=1)

outPut = Label(text="0")
outPut.grid(column=1,row=1)

kmLabel = Label(text="Km")
kmLabel.grid(column=2,row=1)

button = Button(text="Calculate",command=convert)
button.grid(column=1,row=2)
window.mainloop()
