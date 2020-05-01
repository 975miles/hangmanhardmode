import tkinter as tk
from random import randint
from os import listdir

chars = list("abcdefghijklmnopqrstuvwxyz")
unguessed = "_ "
images = listdir("img")
last_guess_num = len(images)

window = tk.Tk()
window.geometry("500x200")
window.title("Hangman hard mode")

def guess(char):
    guessed.append(char)
    
    global incorrect_guesses
    incorrect_guesses = []
    for i in guessed:
        if i not in word:
            incorrect_guesses.append(i)

    global word_display
    word_display = ""
    for i in word:
        if i in guessed:
            word_display += i
        else:
            word_display += unguessed
    
    if unguessed not in word_display: #if the word has now been guessed
        win()
    elif len(incorrect_guesses) == last_guess_num:
        loss()
    else:
        next_turn()


def next_turn():
    clear()
    tk.Label(text=word_display).pack()
    img = tk.PhotoImage(file="img/" + str(len(incorrect_guesses)) + ".gif")
    img_display = tk.Label(image=img)
    img_display.image = img
    img_display.pack()
    
    tk.Label(text="Incorrect guesses: " + ("".join(incorrect_guesses) if len(incorrect_guesses) > 0 else "nothing. Get on with being wrong!")).pack()
    for i in range(len(chars)):
        char = chars[i]
        if char not in guessed:
            tk.Button(text=char, command=lambda char=char: guess(char)).pack(side = tk.LEFT)

    tk.Button(text="I give up", command=loss).pack(side = tk.RIGHT)


def clear():
    for i in window.pack_slaves():
        i.destroy()


def start():
    global word
    global word_display
    word = ""
    word_display = ""
    for i in range(randint(1,12)):
        word += chars[randint(0, len(chars)-1)]
        word_display += unguessed

    global guessed
    global incorrect_guesses
    guessed = []
    incorrect_guesses = []
    
    next_turn()

def win():
    clear()
    tk.Label(text="You guessed \"" + word + "\"?\n I know I couldn't have done that.").pack()
    tk.Button(text="Gain more glory by trying again", command=start).pack()

def loss():
    clear()
    tk.Label(text="You've killed hangman. Well done.\nThat stupid dunce brain of yours couldn't even guess \"" + word + "\"?\n I really did overestimate you.").pack()
    tk.Button(text="Redeem yourself by trying again", command=start).pack()
    


start()

window.mainloop()