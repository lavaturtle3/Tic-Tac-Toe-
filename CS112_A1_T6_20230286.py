#Author : Fras adham
#Description: Tic Tac Toe Game
#Version: 1.0
#Date: 28/2/2024

board = ['1', '2', '3', '4', '5' , '6' ,'7', '8', '9']
def startGame():
    xplayed = False
    counter = 0 #this is use to check if the game is a draw or no
    #if this counter reachs 9 this means the board is full and no one won the game then it's a draw
    drawboard()
    while True:
        if not xplayed:
            try: #validate that the input is an integer
                x = int(input("it's X turn choose a number: "))
            except:
                print("Please input an integer")
                continue
            if board[x-1] != "o" and board[x-1] != "x" and x > 0 and x < 10: #checks if the slot the player choose wasn't choosen before
                updateBoard(x, "x")
                if(winconditions("x")):
                    playagain = input("Play again?? : ")
                    if playagain== "yes":
                        startGame()
                    else:
                        break     
                xplayed = True
                counter += 1
            else:
                print("Play again")  
                continue
        if counter == 9:
            print("It's a draw") 
            playagain = input("Play again?? : ")
            if playagain== "yes":
                startGame()
            else:
                break     
        try:                    
            o = int(input("It's o turn choose a number: "))
        except:
            print("Please input an integer")
            xplayed = True
            continue
        if board[o-1] != "y" and board[o-1] != "x" and o>0 and o<10:
            updateBoard(o, "o")
            if(winconditions("o")):
                playagain = input("Play again?? : ")
                if playagain== "yes":
                    startGame()
                else:
                    break 
            xplayed = False
            counter += 1
        else:
            print("Play again")
            xplayed = True
            continue


def winconditions(char):
    won = False
    winconditions = [board[0] == board[1] and board[1] == board[2] and char, #checks all the win conditions
                                   board[0] == board[3] and board[3] == board[6] and char,
                                   board[0] == board[4] and board[4] == board[8] and char,
                                   board[1] == board[4] and board[4] == board[7] and char,
                                   board[2] == board[4] and board[4] == board[6] and char,
                                   board[2] == board[5] and board[5] == board[8] and char,
                                   board[3] == board[4] and board[4] == board[5] and char,
                                   board[6] == board[7] and board[7] == board[8] and char]
    for win in winconditions:
        if win:
            won = True
            print(char + " Won")
            break
    return won    

def drawboard(): # Draws the board of the game
    slash = "|"
    steps = 0
    for i in range(len(board)):
        print(board[i] ,end=" "+slash+" ")
        steps += 1
        if steps == 3:
            print("")
            steps = 0
def updateBoard(index, char): #updates the board after each player plays
    board[index-1] = char
    drawboard()            
startGame()