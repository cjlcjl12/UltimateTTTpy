a = [' ', ' ', ' ']
b = [' ', ' ', ' ']
c = [' ', ' ', ' ']
#P0 True P1 False
player = True
win = False

def printBoard():
    print(a[0] + " | " + a[1] + " | " + a[2] + "\n" 
        + "---------\n"
        + b[0] + " | " + b[1] + " | " + b[2] + "\n" 
        + "---------\n"
        + c[0] + " | " + c[1] + " | " + c[2])

def makeMove():
    x = input()

    validMove = True
    #check length
    if (len(x) > 2):
        validMove = False
        print("Too long")

    #check letter is a-c
    row = x[0].lower()
    if ((row != 'a') and
        (row != 'b') and
        (row != 'c')):
        validMove = False
        print("Letter out of range " + row)

    col = int(x[1])
    #check number is 0-2
    if (col > 2):
        validMove = False
        print("Number out of range " + str(col))

    if (validMove):
        print("Move was " + x)
        if (row == 'a'):
            if (player):
                a[col] = 'O'
            else:
                a[col] = 'X'
            
        elif (row == 'b'):
            if (player):
                b[col] = 'O'
            else:
                b[col] = 'X'  

        elif (row == 'c'):
            if (player):
                c[col] = 'O'
            else:
                c[col] = 'X'

    else:
        print("Invalid move")

#move formated as A#, B#, C#

printBoard()
while(not(win)):
    if (player):
        print("Player 1 (O's) make your move...")
    else:
        print("Player 2 (X's) make your move...")
    makeMove()
    printBoard()
    player = not(player)
    


