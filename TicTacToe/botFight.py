from tictactoe import TensaiBot, TicTacToe, winner

bot1 = TensaiBot('X')
bot2 = TensaiBot(bot1.marker)
myBoard = TicTacToe()
choice = 'y'
while(choice == 'y'): 
    myBoard.clearBoard()
    myBoard.printBoardGame()
    for i in range(1, 10): 
        if(i%2 == 0): 
            bot1.play(myBoard)
        else: 
            bot2.play(myBoard)
        myBoard.printBoardGame()
        print(myBoard.available)
        print("--------------------")
        if(i >= 5): 
            outcome = winner(myBoard.state, bot1.marker)
            if(outcome == 1): 
                print("Bot 1 Wins")
                break
            elif(outcome == -1): 
                print("Bot 2 Wins")
                break
            elif(i == 9): 
                print("It's a tie")
    choice = input("Do you want to play again? y/n: ").lower()
    while(choice != 'y' and choice != 'n'): 
        choice = input("Y/N: ").lower()