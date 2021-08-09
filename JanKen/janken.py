import random


def janken():
    move = input("Choose your move: ")
    if(move in ["rock", "paper", "scissors"]):
        opponent = random.choice(["rock", "paper", "scissors"])
        print("Computer's move: "+opponent)
        if move == opponent:
            return ""
        elif (move == 'rock' and opponent == 'scissors') or (move == 'scissors' and opponent == 'paper') \
                or (move == 'paper' and opponent == 'rock'):
            return "Win"
        else:
            return "Lose"
    else:
        print("Invalid move! Choose rock, paper or scissors...")
        return ""

choice = 'y'
while(choice.lower() != 'n'):
    win = 0
    lose = 0
    print("Best out of 3\n")
    while(win < 2 and lose <2):
        outcome = janken()
        if(outcome == "Win"): 
            win += 1
        elif(outcome == "Lose"): 
            lose+= 1
        print("\n---------------------\n")
        print("Current Score: ") 
        print("Victories: "+str(win)+" Defeats: "+str(lose)+"\n")
        if(win==2): 
            print("\nYou win!!\n")
        elif(lose == 2): 
            print("\nYou lose...\n")
    choice = input("Do you want to keep playing? y/n: ").lower()
    while(choice != 'y' and choice != 'n'): 
        choice = input("Y/N: ").lower()
