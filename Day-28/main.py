from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
t1 = None
t2 = None


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global t1
    global t2
    marks = ""
    for _ in range((reps-1)//2):
        marks+="✔"
    tick.config(text = marks)
    if reps%2 == 1:
        title_label.config(text = "Work",fg = GREEN)
        counter(30)
        reps+=1
        t1 = window.after(30*1000 + 1000,start_timer)
    else:
        if reps<8:
            title_label.config(text = "Break",fg = RED)
            counter(20)
            reps+=1
            t2 = window.after(20*1000 + 1000,start_timer)
        else:
            reps = 1
            title_label.config(text = "Break",fg = PINK)
            counter(90)

   
       
    
    

def seconds_to_minutes(seconds):
    minutes = seconds//60
    seconds_left = seconds%60

    if seconds_left >=10:
        return f"0{minutes}:{seconds_left}"
    else:
        return f"0{minutes}:0{seconds_left}"
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def counter(count):
    global timer,t1,t2
    if count<0:
        return
   # print(count)
    canvas.itemconfig(canvas_text,text = seconds_to_minutes(count))
    if not t1 or not t2:
        t1 = t2 = timer = window.after(1000,counter,count-1)
    else:
        timer = window.after(1000,counter,count-1)

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    reps = 1
    window.after_cancel(timer)
    window.after_cancel(t1)
    window.after_cancel(t2)
    title_label.config(text = "Timer")
    canvas.itemconfig(canvas_text, text = "00:00")
    tick.config(text = "")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro application")
window.config(padx = 100 , pady = 50,bg = YELLOW)

canvas = Canvas(width = 200, height = 224,bg = YELLOW)
tomato_img = PhotoImage(file ="./Day-28/tomato.png")

canvas.create_image(103,112,image = tomato_img)
canvas_text = canvas.create_text(103,130,text = "00:00",fill = "white",font = (FONT_NAME,35,"bold"))
canvas.grid(row = 1, column = 1)

title_label = Label(text = "Timer",fg = GREEN,bg = YELLOW,font = (FONT_NAME,40,"bold"))
title_label.grid(row = 0, column = 1)

start_button = Button(text = "start",bg = "white",fg = "black", command = start_timer)
start_button.grid(row = 2,column = 0)

reset_button = Button(text = "reset",bg = "white",fg = "black" , command = timer_reset)
reset_button.grid(row = 2,column = 2)

tick = Label(text = "", bg = YELLOW)
tick.grid(row = 3,column = 1)


window.mainloop()