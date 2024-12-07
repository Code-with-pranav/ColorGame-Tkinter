# Import the modules
import tkinter as tk
import random

# List of possible colours
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

# Game variables
score = 0
timeleft = 30
best_score = 0

# Function to start the game
def startGame(event=None):
    global timeleft, score
    if timeleft == 30:
        score = 0
        scoreLabel.config(text=f"Score: {score}")
        countdown()
    nextColour()

# Function to display the next colour
def nextColour():
    global score, timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            global best_score
            score += 1
            best_score = max(best_score, score)
            bestScoreLabel.config(text=f"Best Score: {best_score}")
        e.delete(0, tk.END)
        random.shuffle(colours)
        label.config(fg=colours[1], text=colours[0])
        scoreLabel.config(text=f"Score: {score}")

# Countdown timer function
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text=f"Time left: {timeleft}")
        timeLabel.after(1000, countdown)
    else:
        label.config(text="Game Over!", fg="red")
        restartButton.pack(pady=10)

# Function to restart the game
def restartGame():
    global timeleft, score
    timeleft = 30
    score = 0
    e.delete(0, tk.END)
    scoreLabel.config(text=f"Score: {score}")
    timeLabel.config(text=f"Time left: {timeleft}")
    restartButton.pack_forget()
    label.config(text="")
    startGame()

# Create a GUI window
root = tk.Tk()
root.title("Color Game")
root.geometry("550x340")
root.config(bg="lightblue")

# Fix the size of the window
root.resizable(False, False)

# Instructions
instructions = tk.Label(
    root,
    text="Type the COLOR of the word, not the word text!",
    font=('Arial', 14, 'bold'),
    bg="lightblue",
    fg="darkblue"
)
instructions.pack(pady=10)

# Score label
scoreLabel = tk.Label(
    root,
    text="Press Enter to start",
    font=('Verdana', 12, 'italic'),
    bg="lightblue",
    fg="green"
)
scoreLabel.pack()

# Best score label
bestScoreLabel = tk.Label(
    root,
    text=f"Best Score: {best_score}",
    font=('Verdana', 12, 'italic'),
    bg="lightblue",
    fg="darkgreen"
)
bestScoreLabel.pack()

# Time left label
timeLabel = tk.Label(
    root,
    text=f"Time left: {timeleft}",
    font=('Verdana', 12, 'italic'),
    bg="lightblue",
    fg="red"
)
timeLabel.pack()

# Label for displaying the colors
label = tk.Label(
    root,
    font=('Comic Sans MS', 50, 'bold'),
    bg="lightblue"
)
label.pack(pady=20)


# Text entry box
e = tk.Entry(root, font=('Helvetica', 16))
e.pack()

# Restart button (hidden initially)
restartButton = tk.Button(root, text="Restart Game", font=('Helvetica', 12),
                          bg="white", command=restartGame)

# Bind Enter key to start game
root.bind('<Return>', startGame)

# Set focus on the entry box
e.focus_set()

# Start the GUI
root.mainloop()
