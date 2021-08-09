import random
import math
class Player(): 
    def __init__(self):
        self.marker = ""
        while(self.marker != "X" and self.marker != "O"): 
            self.marker = input("Choose your marker (X or O): ").upper()
    def play(self, myBoard): 
        move = 0
        validMove = False
        while(validMove != True): 
            try: 
                move = int(input("Choose your move: "))
                if(move<1 or move>9): 
                    print("Invalid move, try again")
                elif(myBoard.state[move] != " "): 
                    print("The space is already occupied, try again")
                    myBoard.printBoardGame()
                    print(myBoard.available)
                else: 
                    validMove = True
            except ValueError: 
                print("Invalid move, try again")
        myBoard.state[move] = self.marker
        myBoard.available.remove(move)

class Bot(): 
    def __init__(self, player1): 
        self.marker = ""
        if(player1 == 'X'): 
            self.marker = 'O'
        else: 
            self.marker = 'X'
    def play(self, TicTacToe):
        random.seed()
        move = random.randint(1, 9)
        while(TicTacToe.state[move] != " "): 
            move = random.randint(1, 9)
        TicTacToe.state[move] = self.marker
        TicTacToe.available.remove(move)
        print("CPU's move: ")
class Joe(): 
    def __init__(self, player1):
        self.marker = ""
        if(player1 == 'X'): 
            self.marker = 'O'
        else: 
            self.marker = 'X'
    def play(self, myBoard): 
        random.seed()
        move = 0
        if(random.randint(1, 2) == 1): 
            move = random.randint(1, 9)
            while(myBoard.state[move] != ' '): 
                move = random.randint(1, 9)
        else:
            move = self.minimax(myBoard.state, myBoard.available, self.marker)['Position']
        myBoard.state[move] = self.marker
        myBoard.available.remove(move)
        print("BotJoe's Move: ")
    def minimax(self, state, available, playerMarker): 
        max_player = self.marker
        otherP = 'O' if playerMarker == 'X' else 'X'
        if(winner(state, otherP) == 1):
            score = 0
            if(otherP == max_player): 
                score = len(available)+1
            else: 
                score = -1 * (len(available) +1)
            return {'Position': 0, 'Score': score}
        elif (len(available) == 0): 
            return {'Position': 0, 'Score': 0}
        best = dict()
        if(playerMarker == max_player): 
            best = {'Position': 0, 'Score': -math.inf}
        else: 
            best = {'Position': 0, 'Score': math.inf}
        for x in available: 
            tempAvailable = available.copy()
            state[x] = playerMarker
            tempAvailable.remove(x)
            sim_score = self.minimax(state, tempAvailable, otherP)
            state[x] = " "
            tempAvailable.append(x)
            sim_score['Position'] = x
            if(playerMarker == max_player): 
                if(sim_score['Score'] > best['Score']): 
                    best = sim_score
            else: 
                if(sim_score['Score'] < best['Score']): 
                    best = sim_score
        return best
class TensaiBot(): 
    def __init__(self, player1):
        self.marker = ""
        if(player1 == 'X'): 
            self.marker = 'O'
        else: 
            self.marker = 'X'
    def play(self, myBoard): 
        random.seed()
        move = 0
        if(len(myBoard.available) == 9): 
            move = random.randint(1, 9)
        else:
            move = self.minimax(myBoard.state, myBoard.available, self.marker)['Position']
        myBoard.state[move] = self.marker
        myBoard.available.remove(move)
        print("Tensai's move")
    def minimax(self, state, available, playerMarker): 
        max_player = self.marker
        otherP = 'O' if playerMarker == 'X' else 'X'
        if(winner(state, otherP) == 1):
            score = 0
            if(otherP == max_player): 
                score = len(available)+1
            else: 
                score = -1 * (len(available) +1)
            return {'Position': 0, 'Score': score}
        elif (len(available) == 0): 
            return {'Position': 0, 'Score': 0}
        best = dict()
        if(playerMarker == max_player): 
            best = {'Position': 0, 'Score': -math.inf}
        else: 
            best = {'Position': 0, 'Score': math.inf}
        for x in available: 
            tempAvailable = available.copy()
            state[x] = playerMarker
            tempAvailable.remove(x)
            sim_score = self.minimax(state, tempAvailable, otherP)
            state[x] = " "
            tempAvailable.append(x)
            sim_score['Position'] = x
            if(playerMarker == max_player): 
                if(sim_score['Score'] > best['Score']): 
                    best = sim_score
            else: 
                if(sim_score['Score'] < best['Score']): 
                    best = sim_score
        return best
class TicTacToe(): 
    def __init__(self):
        self.state = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
        self.available = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def printBoardGame(self): 
        print(self.state[7]+"|"+self.state[8]+"|"+self.state[9])
        print("-+-+-")
        print(self.state[4]+"|"+self.state[5]+"|"+self.state[6])
        print("-+-+-")
        print(self.state[1]+"|"+self.state[2]+"|"+self.state[3])
    def clearBoard(self): 
        self.available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(1, 10):
            self.state[i] = " "

def winner(myBoard, player1): 
    playerWinner = False 
    botWinner = False
    for i in range(1, 8, 3): 
        if(myBoard[i] == myBoard[i+1] == myBoard[i+2] != " "): 
            if(myBoard[i] == player1): 
                playerWinner = True; 
            else: 
                botWinner = True; 
            break; 
    for i in range(1, 4, 1): 
        if(myBoard[i] == myBoard[i+3] == myBoard[i+6] != " "): 
            if(myBoard[i] == player1): 
                playerWinner = True; 
            else: 
                botWinner = True
            break
    if(myBoard[1] == myBoard[5] == myBoard[9] != " "): 
        if(myBoard[1] == player1): 
            playerWinner = True; 
        else: 
            botWinner = True; 
    elif(myBoard[3] == myBoard[5] == myBoard[7] != " "): 
        if(myBoard[3] == player1): 
            playerWinner = True; 
        else: 
            botWinner = True; 
    if(playerWinner): 
        return 1
    elif(botWinner):
        return -1
    else: 
        return 0