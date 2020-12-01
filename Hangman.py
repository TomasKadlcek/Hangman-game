from random_word import RandomWords
from tkinter import *
from tkinter import messagebox
import turtle

#### Please mind this was a total begginer project...

root = Tk()
root.title("Hangman")
root.iconbitmap("icona.ico")
root.geometry("245x580+300+300")


level = IntVar()
guess_letter = StringVar()
f_letter = StringVar()
empty_guess2 = StringVar()
rand_word = StringVar()
fill_guess = StringVar()
counter = 0
bins = ["Already used: "]
binned = "Already used: "


def guess_len(event=None):
    global text_prompt
    global input_win
    global sub_button
    global out_win
    global num
    global f_letter
    global empty_guess2
    global rand_word

    try:
        num = level.get()
    except TclError:
        text_prompt.grid_forget()
        text_prompt = Label(root, text="How many letters should the word have?\nOnly digits.", width=30)
        text_prompt.grid(row=0, column=0, padx=15)
        input_win = Entry(root, textvariable=level, width=30, justify=CENTER)
        input_win.select_range(0, END)
        input_win.grid(row=1, column=0, padx=15)
        input_win.focus_set()
        input_win.bind('<Return>', guess_len)
        num = level.get()
        sub_button = Button(root, text="Submit", command=guess_len)
        sub_button.grid(row=2, column=0, padx=15)
        out_win = Label(root, relief=SUNKEN, width=30)
        out_win.grid(row=3, column=0, padx=15)

    lib = RandomWords()
    rand_word = lib.get_random_word(minLength=num, maxLength=num).lower()
    empty_guess = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    empty_guess2 = empty_guess[0:len(rand_word)]
    input_win.delete(0, END)
    text_prompt.grid_forget()
    out_win.grid_forget()
    text_prompt = Label(root, text="Guess a letter.", width=30)
    text_prompt.grid(row=0, column=0, padx=15)
    input_win.grid_forget()
    input_win = Entry(root, textvariable=guess_letter, width=30, justify=CENTER)
    input_win.grid(row=1, column=0, padx=15)
    input_win.focus_set()
    input_win.bind('<Return>', send_letter)
    f_letter = guess_letter.get()
    sub_button = Button(root, text="Submit", command=send_letter)
    sub_button.grid(row=2, column=0, padx=15)
    out_win = Label(root, relief=SUNKEN, text=empty_guess2, width=30)
    out_win.grid(row=3, column=0, padx=15)


def send_letter(event=None):
    global text_prompt
    global input_win
    global sub_button
    global out_win
    global guess_letter
    global f_letter
    global empty_guess2
    global rand_word
    global fill_guess
    global num
    global level
    global counter
    global binned
    global bins
    global guessed
    f_letter = guess_letter.get()
    while True:
        if len(f_letter) != 1:
            input_win.delete(0, END)
            text_prompt.grid_forget()
            out_win.grid_forget()
            text_prompt = Label(root, text="Max 1 letter.", width=30)
            text_prompt.grid(row=0, column=0, padx=15)
            input_win.grid_forget()
            input_win = Entry(root, textvariable=guess_letter, width=30, justify=CENTER)
            input_win.grid(row=1, column=0, padx=15)
            input_win.focus_set()
            input_win.bind('<Return>', send_letter)
            sub_button = Button(root, text="Submit", command=send_letter)
            sub_button.grid(row=2, column=0, padx=15)
            out_win = Label(root, relief=SUNKEN, text=fill_guess, width=30)
            out_win.grid(row=3, column=0, padx=15)
            break
        if f_letter in rand_word:
            for i in rand_word:
                lst = [i for i, n in enumerate(rand_word) if n == f_letter]
                for e in lst:
                    empty_guess2[e] = f_letter
                    input_win.delete(0, END)
                if list(rand_word) == empty_guess2:
                    fill_guess = "".join(empty_guess2)
                    again = messagebox.askyesno("New game?", "Correct, answer is " + fill_guess + "\nDo you wish to play again??")
                    if again == 1:
                        loop()
                        return False
                    if again == 0:
                        raise SystemExit
            fill_guess = "".join(empty_guess2)
            input_win.delete(0, END)
            text_prompt.grid_forget()
            out_win.grid_forget()
            text_prompt = Label(root, text="Guess a letter.", width=30)
            text_prompt.grid(row=0, column=0, padx=15)
            input_win.grid_forget()
            input_win = Entry(root, textvariable=guess_letter, width=30, justify=CENTER)
            input_win.grid(row=1, column=0, padx=15)
            input_win.focus_set()
            input_win.bind('<Return>', send_letter)
            sub_button = Button(root, text="Submit", command=send_letter)
            sub_button.grid(row=2, column=0, padx=15)
            out_win = Label(root, relief=SUNKEN, text=fill_guess, width=30)
            out_win.grid(row=3, column=0, padx=15)
            break
        else:
            if f_letter.upper() not in bins:
                bins.append(guess_letter.get())
                bins = [b.capitalize() for b in bins]
                binned = " ".join(bins)
            fill_guess = "".join(empty_guess2)
            input_win.delete(0, END)
            text_prompt.grid_forget()
            out_win.grid_forget()
            guessed.grid_forget()
            text_prompt = Label(root, text="Wrong guess. Guess a letter.", width=30)
            text_prompt.grid(row=0, column=0, padx=15)
            input_win.grid_forget()
            input_win = Entry(root, textvariable=guess_letter, width=30, justify=CENTER)
            input_win.focus_set()
            input_win.bind('<Return>', send_letter)
            input_win.grid(row=1, column=0, padx=15)
            sub_button = Button(root, text="Submit", command=send_letter)
            sub_button.grid(row=2, column=0, padx=15)
            out_win = Label(root, relief=SUNKEN, text=fill_guess, width=30)
            out_win.grid(row=3, column=0, padx=15)
            counter += 1
            guessed = Label(root, width=30, text=binned)
            guessed.grid(row=4, column=0, padx=15)

            if counter == 1:
                shape1 = turtle.RawPen(canvas)
                shape1.speed(0)
                shape1.shape("square")
                shape1.color("black")
                shape1.shapesize(stretch_wid=1, stretch_len=7)
                shape1.penup()
                shape1.goto(-30, -180)

            if counter == 2:
                shape2 = turtle.RawPen(canvas)
                shape2.speed(0)
                shape2.shape("square")
                shape2.color("black")
                shape2.shapesize(stretch_wid=15, stretch_len=1)
                shape2.penup()
                shape2.goto(-80, -20)

            if counter == 3:
                shape3 = turtle.RawPen(canvas)
                shape3.speed(0)
                shape3.shape("square")
                shape3.color("black")
                shape3.shapesize(stretch_wid=1, stretch_len=9)
                shape3.penup()
                shape3.goto(0, 140)

            if counter == 4:
                shape4 = turtle.RawPen(canvas)
                shape4.speed(0)
                shape4.left(45)
                shape4.shape("square")
                shape4.color("black")
                shape4.shapesize(stretch_wid=1, stretch_len=3)
                shape4.penup()
                shape4.goto(-55, 115)

            if counter == 5:
                shape5 = turtle.RawPen(canvas)
                shape5.speed(0)
                shape5.shape("square")
                shape5.color("black")
                shape5.shapesize(stretch_wid=4, stretch_len=1)
                shape5.penup()
                shape5.goto(40, 105)

            if counter == 6:
                shape6 = turtle.RawPen(canvas)
                shape6.speed(0)
                shape6.shape("circle")
                shape6.color("black")
                shape6.shapesize(stretch_wid=2, stretch_len=2)
                shape6.penup()
                shape6.goto(40, 60)

            if counter == 7:
                shape7 = turtle.RawPen(canvas)
                shape7.speed(0)
                shape7.shape("square")
                shape7.color("black")
                shape7.shapesize(stretch_wid=4, stretch_len=1)
                shape7.penup()
                shape7.goto(40, 0)

            if counter == 8:
                shape8 = turtle.RawPen(canvas)
                shape8.left(45)
                shape8.speed(0)
                shape8.shape("square")
                shape8.color("black")
                shape8.shapesize(stretch_wid=3, stretch_len=1)
                shape8.penup()
                shape8.goto(65, 10)

            if counter == 9:
                shape9 = turtle.RawPen(canvas)
                shape9.right(45)
                shape9.speed(0)
                shape9.shape("square")
                shape9.color("black")
                shape9.shapesize(stretch_wid=3, stretch_len=1)
                shape9.penup()
                shape9.goto(15, 10)

            if counter == 10:
                shape10 = turtle.RawPen(canvas)
                shape10.left(30)
                shape10.speed(0)
                shape10.shape("square")
                shape10.color("black")
                shape10.shapesize(stretch_wid=4, stretch_len=1)
                shape10.penup()
                shape10.goto(60, -70)

            if counter == 11:
                shape11 = turtle.RawPen(canvas)
                shape11.right(30)
                shape11.speed(0)
                shape11.shape("square")
                shape11.color("black")
                shape11.shapesize(stretch_wid=4, stretch_len=1)
                shape11.penup()
                shape11.goto(20, -70)

            if counter == 12:
                again = messagebox.askyesno("New game?",
                                            "Correct, answer is " + rand_word + "\nDo you wish to play again??")
                if again == 1:
                    loop()
                    counter = 0
                    canvas.delete("all")
                    return False
                if again == 0:
                    raise SystemExit
            break


def loop(event=None):
    global text_prompt
    global input_win
    global num
    global sub_button
    global out_win
    global level
    global guess_letter
    global f_letter
    global empty_guess2
    global rand_word
    global fill_guess
    global counter
    global bins
    global guessed
    global binned
    level = IntVar()
    guess_letter = StringVar()
    f_letter = StringVar()
    empty_guess2 = StringVar()
    rand_word = StringVar()
    fill_guess = StringVar()
    bins = ["Already used: "]
    binned = "Already used: "
    counter = 0
    canvas.delete("all")
    text_prompt.grid_forget()
    input_win.delete(0, END)
    sub_button.grid_forget()
    out_win.grid_forget()
    guessed.grid_forget()
    text_prompt = Label(root, text="How many letters should the word have?", width=30)
    text_prompt.grid(row=0, column=0, padx=15)
    input_win = Entry(root, textvariable=level, width=30, justify=CENTER)
    input_win.select_range(0, END)
    input_win.grid(row=1, column=0, padx=15)
    input_win.focus_set()
    input_win.bind('<Return>', guess_len)
    sub_button = Button(root, text="Submit", command=guess_len)
    sub_button.grid(row=2, column=0, padx=15)
    out_win = Label(root, relief=SUNKEN, width=30)
    out_win.grid(row=3, column=0, padx=15)
    guessed = Label(root, width=30, text=binned)
    guessed.grid(row=4, column=0, padx=15)

#
# def hello():
#     return


menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

text_prompt = Label(root, text="How many letters should the word have?", width=30)
text_prompt.grid(row=0, column=0, padx=15)
input_win = Entry(root, textvariable=level, width=30, justify=CENTER)
input_win.select_range(0, END)
input_win.grid(row=1, column=0, padx=15)
input_win.focus_set()
input_win.bind('<Return>', guess_len)
num = level.get()
sub_button = Button(root, text="Submit", command=guess_len)
sub_button.grid(row=2, column=0, padx=15)
out_win = Label(root, relief=SUNKEN, width=30)
out_win.grid(row=3, column=0, padx=15)
guessed = Label(root, width=30, text=binned)
guessed.grid(row=4, column=0, padx=15)
reset = Button(root, text="Restart", command=loop)
reset.grid(row=6, column=0, padx=15)

canvas = Canvas(root, width=200, height=400)
canvas.grid(row=5, column=0, padx=15)


root.mainloop()