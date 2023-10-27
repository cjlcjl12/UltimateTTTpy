import tttfuncs

tttfuncs.printBoard()

while(not(tttfuncs.win)):
    if (tttfuncs.player):
        print("Player 1 (O's) make your move...")
    else:
        print("Player 2 (X's)q' make your move...")

    tttfuncs.makeMove()
    tttfuncs.printBoard()
    tttfuncs.win = tttfuncs.checkWin()

    #change active player
    tttfuncs.player = not(tttfuncs.player)
    
