from random import randint

def win():
    print ('You win!')

def lose():
    print ('You lose!')
while True:
    player_choice = input("What do you pick? (rock, paper, scissors")
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = [random_move]

    if player_choice == computer_choice:
        print ("Draw!")
    elif player_choice == 'rock' or computer_choice == 'scissors':
        win()
        print("ypur player choice is rock and computer choice is scissors,you win!")
    elif  player_choice== 'paper' or computer_choice == 'scissors':
        lose()
        print("ypur player choice is rock and computer choice is scissors,you lose!")
    elif player_choice == 'scissors' or computer_choice == 'paper':
       win()
       print("ypur player choice is rock and computer choice is scissors,you win!")
    elif player_choice == 'scissors' or computer_choice == 'rock':
       lose()
       print("ypur player choice is rock and computer choice is scissors,you lose!")
    elif player_choice == 'paper' or  computer_choice== 'rock':
        win()
        print("ypur player choice is rock and computer choice is scissors,you win!")
    elif player_choice=="rock"  or computer_choice =="paper" :
        lose()
        print("ypur player choice is rock and computer choice is scissors,you lose!")
    again = input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break 
# Edit on Github