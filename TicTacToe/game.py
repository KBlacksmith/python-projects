import tictactoe
import random
human = tictactoe.Player()
player1 = None
player2 = None
enemyBot = None
myBoard = tictactoe.TicTacToe()
random.seed()
choice = "y"
while(choice != "n"): 
    print("Choose difficulty")
    level = -1
    while(level <1 or level >3): 
        try: 
            level = int(input("1--Easy/2--Medium/3--Hard: "))
        except ValueError: 
            print("Invalid difficulty")
    if(level == 1): 
        enemyBot = tictactoe.Bot(human.marker)
    elif(level == 2): 
        enemyBot = tictactoe.Joe(human.marker)
    else: 
        enemyBot = tictactoe.TensaiBot(human.marker)
    myBoard.clearBoard()
    myBoard.printBoardGame()
    print(myBoard.available)
    print("-----------------")
    if(random.randint(1, 2) == 1): 
        player1 = human
        player2 = enemyBot
        pass
    else: 
        player1 = enemyBot
        player2 = human
    for i in range(1, 10): 
        if(i%2 == 1): 
            player1.play(myBoard)
        else: 
            player2.play(myBoard)
        myBoard.printBoardGame()
        print(myBoard.available)
        print("-----------------")
        if(i>=5): 
            outcome = tictactoe.winner(myBoard.state, human.marker)
            if(outcome == 1): 
                print("Congratulations, you win!")
                break
            elif(outcome == -1): 
                print("Sorry, you lose...")
                break
            elif(i == 9): 
                print("It's a tie!")
    choice = input("Do you want to play again? y/n: ").lower()
    while(choice != 'y' and choice != 'n'): 
        choice = input("Y/N: ").lower()