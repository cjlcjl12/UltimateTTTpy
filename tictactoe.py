import funcs

funcs.printBoard()

while(not(funcs.win)):
    if (funcs.player):
        print("Player 1 (O's) make your move...")
    else:
        print("Player 2 (X's) make your move...")

    funcs.makeMove()
    funcs.printBoard()
    funcs.win = funcs.checkWin()

    #change active player
    funcs.player = not(funcs.player)
    
