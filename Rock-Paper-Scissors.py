'''importing modules tkinter and random'''
import tkinter as tk
import random

'''creating the main window and giving title to it'''
root = tk.Tk()
root.title('Rock-Paper-Scissors')

'''creating scores variables and one to store the
game result'''
player_score = 0
computer_score = 0
tie_score = 0
game_result = ''

'''creating  output label to show output 
on window itself'''
output_label = tk.Label(root,text = '')
output_label.pack()

'''creating label for score and using pack making it 
visible to the main window'''
score_label = tk.Label(root,text = f'Player :{player_score} -'
                                   f'Computer : {computer_score}-'
                                   f'Tie : {tie_score}')
score_label.pack()

'''creating functions to update scores and 
game results'''
def update_score():
    score_label.config(text = f'Player : {player_score} - '
                               f'Computer : {computer_score}-'
                              f'Tie : {tie_score}')
def update_result():
    output_label.config(text=f'{game_result}')

'''creating main game function'''
def play(player_choice):
    global player_score,computer_score,tie_score,game_result

    computer_choice = random.choice(['Rock','Paper',
                                    'Scissors'])

    if player_choice == computer_choice:
        game_result = 'Tie!'
        tie_score += 1
    elif player_choice == 'Rock':
        if computer_choice == 'Scissors':
            game_result = 'You Win'
            player_score += 1
        else:
            game_result = 'You Lose'
            computer_score += 1
    elif player_choice == 'Paper':
        if computer_choice == 'Rock':
            game_result = 'You Win'
            player_score += 1
        else:
            game_result = 'You Lose'
            computer_score += 1
    elif player_choice == 'Scissors':
        if computer_choice == 'Paper':
            game_result = 'You Win'
            player_score += 1
        else:
            game_result = 'You Lose'
            computer_score += 1
    else:
        print('Put a valid input, Check your spelling!')

    update_result()
    update_score()

'''creating buttons for player choice'''
rock_button = tk.Button(root,text = 'Rock',command =
                        lambda :play('Rock'))
rock_button.pack()

paper_button = tk.Button(root,text = 'Paper',command =
                         lambda :play('Paper'))
paper_button.pack()

scissors_button = tk.Button(root,text = 'Scissors',command=
                            lambda:play('Scissors'))
scissors_button.pack()

root.mainloop()




























