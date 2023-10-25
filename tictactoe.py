a = [' ', ' ', ' ']
b = [' ', ' ', ' ']
c = [' ', ' ', ' ']
#P1 True P2 False
player = True
win = False

def printBoard():
    print("\n"
        + a[0] + " | " + a[1] + " | " + a[2] + "\n" 
        + "---------\n"
        + b[0] + " | " + b[1] + " | " + b[2] + "\n" 
        + "---------\n"
        + c[0] + " | " + c[1] + " | " + c[2]
        + "\n")

def makeMove():
    moveComplete = False

    while(not(moveComplete)):
        validMove = True
        x = input()

        if (x=="q"):
            print("Exiting...")
            exit()

        #check length
        if (len(x) != 2):
            validMove = False
            print("Bad length")

        #check letter is a-c
        row = x[0].lower()
        if ((row != 'a') and
            (row != 'b') and
            (row != 'c')):
            validMove = False
            print("Letter out of range " + row)

        col = 999

        #Check if digit in position 2
        if(validMove):
            if (x[1].isdigit()):
                print(x[1] + " is a number")
                col = int(x[1])
            else:
                print("Not a number")
                validMove = False

        #check number is 0-2
        if (col > 2):
            validMove = False
            print("Number out of range " + str(col))

        if (validMove):
            if (row == 'a') and (a[col] == ' '):
                if (player):
                    a[col] = 'O'
                else:
                    a[col] = 'X'
                moveComplete = True
                
            elif (row == 'b') and (b[col] == ' '):
                if (player):
                    b[col] = 'O'
                else:
                    b[col] = 'X'  
                moveComplete = True

            elif (row == 'c') and (c[col] == ' '):
                if (player):
                    c[col] = 'O'
                else:
                    c[col] = 'X'
                moveComplete = True
            else:
                print("Position occupied.\nTry again...")
        else:
            print("Try again...")

def checkWin():
    winLocal = False
    #vertical
    if (a[0] == b[0] == c[0]) and (a[0] != ' '):
        winLocal = True
    elif (a[1] == b[1] == c[1]) and (a[1] != ' '):
        winLocal = True
    elif (a[2] == b[2] == c[2]) and (a[2] != ' '):
        winLocal = True

    #horizontal
    if (a[0] == a[1] == a[2]) and (a[0] != ' '):
        winLocal = True
    elif (b[0] == b[1] == b[2]) and (b[0] != ' '):
        winLocal = True
    elif (c[0] == c[1] == c[2]) and (c[0] != ' '):
        winLocal = True

    #diagonal
    if (a[0] == b[1] == c[2]) and (a[0] != ' '):
        winLocal = True
    elif (a[2] == b[1] == c[0]) and (a[2] != ' '):
        winLocal = True

    if(winLocal):
        if (player):
            pNum = 1
        else:
            pNum = 2

        print("Victory! Congrats Player " + str(pNum))
        return True
    
    return False
printBoard()

while(not(win)):
    if (player):
        print("Player 1 (O's) make your move...")
    else:
        print("Player 2 (X's) make your move...")

    makeMove()
    printBoard()
    win = checkWin()

    #change active player
    player = not(player)
    
