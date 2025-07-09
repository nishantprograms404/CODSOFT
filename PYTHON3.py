import tkinter as tk
import random

#initial scores
user_score = 0
computer_score = 0

#Options
options = ['Rock', 'Paper', 'Scissors']

#Game Logic
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        user_score += 1
        result = "You win!"
    else:
        computer_score += 1
        result = "Computer Wins!"

    result_label.config(text=f"You chose{user_choice} | Computer chose {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | {computer_score}")

#Reset Function
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Score - You: 0 | Computer:0")

#GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

#Title
tk.Label(root, text="Rock Paper Scissor Game", font=("Arial",16)).pack(pady=10)


#Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for choice in options:
    tk.Button(button_frame, text=choice, width=10, command=lambda c=choice:play(c)).pack(side='left',padx=10)

#Result label
result_label = tk.Label(root, text="Make your move!",font=("Arial",12))
result_label.pack(pady=20)

#Score label
score_label = tk.Label(root, text="Score - You: 0 | Computer:0", font=("Arial",12))
score_label.pack()

#Reset and Quit Buttons
control_frame = tk.Frame(root)
control_frame.pack(pady=20)

tk.Button(control_frame, text="Reset", bg="orange", fg="white", command=reset_game).pack(side='left',padx=20)
tk.Button(control_frame, text="Quit", bg="red",fg="white",command=root.quit).pack(side='right',padx=20)

#Main loop
root.mainloop()


        
