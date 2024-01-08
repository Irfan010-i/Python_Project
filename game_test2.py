# MAIN CODE FOR NOW !!!!
from tkinter import *
import tkinter.font as font
import random
from tkinter import *
import tkinter.font as font
import random
# List of colors
colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]

# Variables for timer, score, and displayed word color
timer = 60
score = 0
displayed_word_color = ''

# Create a list to store previous high scores
high_scores = []

# Function to update high scores
def updateHighScores():
    global score, high_scores
    # Add current score to high scores list
    high_scores.append(score)
    # Sort high scores list in descending order
    high_scores.sort(reverse=True)
    # Keep only the top 5 high scores
    high_scores = high_scores[:5]
    # Open a new window to display high scores
    high_scores_window = Toplevel(my_window)
    high_scores_window.title("High Scores")
    high_scores_window.geometry("300x200")
    # Display current score and high scores in labels
    current_score_label = Label(high_scores_window, text="Your Score: " + str(score))
    current_score_label.pack()
    high_scores_label = Label(high_scores_window, text="High Scores:")
    high_scores_label.pack()
    for i, score in enumerate(high_scores):
        score_label = Label(high_scores_window, text=str(i+1) + ". " + str(score))
        score_label.pack()

# Function to start the game
def startGame():
    global displayed_word_color, timer, score
    # Start the countdown timer
    if(timer == 60):
        startCountDown()
        # Choose a random color and display it in a label
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text=random.choice(colors), fg=displayed_word_color)
        # Bind the Return key to the displayNextWord function
        color_entry.bind('<Return>', displayNextWord)
        # Reset the score
        score = 0
        game_score.config(text="Your Score : " + str(score))

# Function to reset the game
def resetGame():
    global timer, score, displayed_word_color
    timer = 60
    score = 0
    displayed_word_color = ''
    game_score.config(text="Your Score : " + str(score))
    display_words.config(text='')
    time_left.config(text="Game Ends in : -")
    color_entry.delete(0, END)

# Function to start the countdown timer
def startCountDown():
    global timer
    if(timer >= 0):
        time_left.config(text="Game Ends in : " + str(timer) + "s")
        timer -= 1
        time_left.after(1000, startCountDown)
        if (timer == -1):
            time_left.config(text="Game Over!!!")
            # Update high scores when game is over
            updateHighScores()

# Function to display the next word and update the score
def displayNextWord(event):
    global displayed_word_color, score
    if(timer > 0):
        if(displayed_word_color == color_entry.get().lower()):
            score += 1
            game_score.config(text="Your Score : " + str(score))
        color_entry.delete(0, END)
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text=random.choice(colors), fg=displayed_word_color)


# Create the main window
my_window = Tk()
my_window.title("Color Game")
my_window.geometry("500x250")

app_font = font.Font(family='Helvetica', size = 12)

# creating a label to display description to on the interface
game_desp = "Game Description: Enter the color of the words displayed below. \n And Keep in mind not to enter the word text itself. \n Go away if COLOUR BLIND......"
myFont = font.Font(family='Helvetica')

game_description = Label(my_window, text = game_desp, font = app_font, fg= "grey")
game_description.pack()

# Create a label to display the timer
time_left = Label(my_window, text = "Game Ends in : -", font = (font.Font(size=14)), fg = "orange")
time_left.pack()

# Create a label to display the current score
game_score = Label(my_window, text="Your Score : 0", font=('Helvetica', 12, 'bold'))
game_score.pack()

# Create a label to display the random words in a different color
display_words = Label(my_window, font=('Helvetica', 60))
display_words.pack()

# Create an entry field for the user to type in the color of the displayed word
color_entry = Entry(my_window, font=('Helvetica', 14))
color_entry.pack(pady=10)


# Create a button to start the game
# start_button = Button(my_window, text = "Start", width = 20, fg = "black", bg = "pink", bd = 0,padx = 20, pady=10,command=startGame)
# start_button.pack(side=LEFT, padx=10)

# Create a button to reset the game
# reset_button = Button(my_window, text = "Reset", width = 20, fg = "black", bg = "light blue", bd = 0,padx = 20, pady = 10 , command = resetGame)
# reset_button.pack(side=LEFT, padx=10)

btn_frame = Frame(my_window, width= 80, height = 40, bg= 'red')
btn_frame.pack(side = BOTTOM)

start_button = Button(btn_frame, text = "Start", width = 20, fg = "black", bg = "pink", bd = 0,padx = 20, pady = 10 , command = startGame)
start_button.grid(row=0, column= 0)

reset_button = Button(btn_frame, text = "Reset", width = 20, fg = "black", bg = "light blue", bd = 0,padx = 20, pady = 10 , command = resetGame)
reset_button.grid(row=0, column= 1)


my_window.geometry('600x300')
my_window.mainloop()


