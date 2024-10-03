from tkinter import *
import pandas as pd
import random

# constant for frequently used colors
BG = "#faf8f6"
Purple = '#800080'
plum = '#673147'
current_word = {}
words_to_learn = {}

try:
    """ if the app will use the unknown words if it's used before skipping the known words if it's first of the
    user have no known koren words it starts from the complete full csv file """
    data = pd.read_csv("data/unknown_words.csv")
except FileNotFoundError:
    complete_data = pd.read_csv("data/output.csv")
    words_to_learn = complete_data.to_dict(orient='records')
else:
    words_to_learn = data.to_dict(orient='records')


def translate():
    """after 3 sec if not pressed either buttons the card will flip and display the translation for that word"""
    current_english_word = current_word['English']
    canvas.itemconfig(lang, text='English',fill=Purple)
    canvas.itemconfig(word, text=current_english_word,fill=Purple)
    canvas.itemconfig(lang_bg,image=logo_img_2)


def next_word():
    """ goes to the next korean word to learn"""
    global current_word,delay_flipping
    canvas.itemconfig(lang_bg, image=logo_img)
    current_word = random.choice(words_to_learn)
    current_korean_word = current_word['Korean']
    canvas.itemconfig(word,text=current_korean_word,fill=plum)
    canvas.itemconfig(lang, text='Korean',fill=plum)
    window.after_cancel(delay_flipping)
    delay_flipping = window.after(3000,func=translate)


def known_word():
    """"if the user pressed the check mark 'knows the word' then it will be removed from the output file
    as if the user starts the app again, so it'll save the user's progress"""
    words_to_learn.remove(current_word)
    next_word()
    unknown_words = pd.DataFrame(words_to_learn)
    unknown_words.to_csv("data/unknown_words.csv",index=False)


# UI buttons, window and images set up
window = Tk()
window.config(padx=50,pady=50,bg=BG)
window.title("Korean flashcards")
delay_flipping = window.after(3000, func=translate)

canvas = Canvas(width=600,height=500,bg=BG, highlightthickness=0)
logo_img = PhotoImage(file='images/1.png')
logo_img_2 = PhotoImage(file='images/2.png')

lang_bg = canvas.create_image(300,250,image =logo_img)
lang = canvas.create_text(300,170,font=('Ariel',20,"italic"))
word = canvas.create_text(300,250,font=('Ariel',40,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

my_image = PhotoImage(file="images/f.png",height=100,width=100)
button_wrong = Button(image=my_image, highlightthickness=0,bg=BG,command=next_word)
button_wrong.grid(row=1,column=0)

my_image2 = PhotoImage(file="images/t.png",height=100,width=100)
button_right = Button(image=my_image2, highlightthickness=0, bg=BG, command=known_word)
button_right.grid(row=1,column=1)

next_word()
window.mainloop()
