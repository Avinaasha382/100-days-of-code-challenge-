THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:
    def __init__(self,quiz):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20,pady = 20,bg = THEME_COLOR)
        self.score_label = Label(text = "Score:0",fg = "white",bg = THEME_COLOR)
        self.score_label.grid(row = 0, column=1)
        self.canvas = Canvas(width = 300, height = 250,bg = "white")
        self.canvas_text = self.canvas.create_text(150,125,text = "Hi",font = ("Arial",20,"italic"),width = 280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady = 50)
        true_image = PhotoImage(file = "images/true.png")
        self.right_button = Button(image = true_image,highlightthickness=0,command = self.right_answer)
        self.right_button.grid(row=2,column=0)
        wrong_image = PhotoImage(file = "./images/false.png")
        self.wrong_button = Button(image = wrong_image,highlightthickness = 0,command = self.wrong_answer)
        self.wrong_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text = q_text)
        else:
            self.right_button.config(state = "disabled")
            self.wrong_button.config(state="disabled")
            self.canvas.itemconfig(self.canvas_text,text = "Congratulations!!, you have reached the end of the quiz..")
    
    def right_answer(self):
        is_right = self.quiz.check_answer("True")
        self.check_answer(is_right)
        
    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.check_answer(is_right)
    
    def check_answer(self,is_right:bool):
        if(is_right == True):
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        
        self.window.after(1000,self.display_next_question)
    
    def display_next_question(self):
        self.canvas.config(bg = "white")
        self.get_next_question()

