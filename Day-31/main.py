from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

#reading data from the csv file:
try:
    df = pd.read_csv("./words_to_know.csv")
    print("New file exists")
except:
    df = pd.read_csv("./data/french_words.csv")
    print("Still using old data")
finally:
    data = df.to_dict(orient="records")
flip_timer = None


def generate_english_translation(word):
    window.after_cancel(flip_timer)
    language_label.config(text = "English")
    word_label.config(text = word['English'] )
    canvas.itemconfig(canvas_image, image=card_back_image) 
    

def generate_new_word():
    global flip_timer
    language_label.config(text = "French")
    canvas.itemconfig(canvas_image,image = card_front_image)
    word = random.choice(data)
    word_label.config(text = word['French'])
    flip_timer = window.after(3000,generate_english_translation,word)
    return word

def known_word():
    word = generate_new_word()
    data.remove(word)
    

    val = pd.DataFrame(data)
    print(val)
    val.to_csv("words_to_know.csv",index = False)


def unknown_word():
    generate_new_word()



window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50,bg = BACKGROUND_COLOR)

canvas = Canvas(width = 800,height = 526,highlightthickness=0)
card_front_image = PhotoImage(file = "./images/card_front.png")
card_back_image = PhotoImage(file = "./images/card_back.png")
canvas_image = canvas.create_image(400,263,image = card_front_image)
canvas.grid(row = 0, column = 0,columnspan=2)

language_label = Label(text = "French",font = ("Ariel",40,"italic"))
language_label.place(x = 300, y = 150)

word_label = Label(text ="",font = ("Ariel",60,"bold"))
word_label.place(x = 300, y = 263)

right_image = PhotoImage(file = "./images/right.png")
wrong_image = PhotoImage(file = "./images/wrong.png")

right_button = Button(image = right_image,highlightthickness=0,command = known_word)
right_button.grid(row = 1,column = 0)

wrong_button = Button(image = wrong_image,highlightthickness=0,command = unknown_word)
wrong_button.grid(row = 1,column = 1)

known_word()








window.mainloop()


