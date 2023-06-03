import copy
import itertools

"""
this minmax ai will rate the tictactoe board and moves from -1 to 1
the number represents how many moves in till the ai will win or lose
the score furtest from 0 will be selected as it will either maximze the ai's postion or minimize the players position
"""



###################### functions ######################

# find a winner #
def getwinner(board,player,lasty):
    if board[lasty] == [player,player,player]:
        return True
    if (board[0][0] == player and board[1][0] == player and board[2][0] == player) or (board[0][2] == player and board[1][2] == player and board[2][2] == player):
        return True
    if (board[1][1] == player) and ((board[0][0] == player and board[2][2] == player) or (board[0][2] == player and board[2][0] == player) or (board[0][1] == player and board[2][1] == player)):
        return True
#################

# find moves #
def getavliblemoves(board):
    moves = []
    for i in range(len(board)):# rows
        for j in range(len(board)):# collums
            if board[i][j] != "O":# find all moves on board
                if board[i][j] != "X":
                    moves.append([i,j])
    return(moves)
##############

# minmax ai #
def minmax(nboard,moves,player): # 
    try:
        for i in range(len(moves)):
            for j in range(len(moves)):
                nboard[moves[i][0]][moves[i][1]] = player
                gamestateplayer = getwinner(nboard,"O",moves[i][0])
                gamestateopp = getwinner(nboard,"X",moves[i][0])
                if gamestateopp == True:
                    return(-1/(1+j+(i*3)))
                elif gamestateplayer == True:
                    return(1/(1+j+(i*3)))
                # change turn
                if player == "O":
                    player = "X"
                else:
                    player = "O"
                try:

                    moves.remove(moves[i])
                except(AttributeError):
                    pass
        return(0)

    except(IndexError):
        print("error")
#############

# minmax 2 #
def minmax2(board):
    moves = getavliblemoves(board)
    allsolutions = list(itertools.permutations(moves))
    Maxscore = -1000
    Minscore = 1000
    rep = 0
    for i in allsolutions:
        rep += 1
        c_board = copy.deepcopy(board)
        score = minmax(c_board,i,"O")
        print(f"moves = {i}\n score = {score} \nrepitions : {rep}")
        if score < Minscore:
            Minscore = score
            Minmoves = i
            pass
        elif score > Maxscore:
            Maxscore = score
            Maxmoves = i
        rep += 1
    if (Minscore*Minscore) >= Maxscore:# find the lowest or highest score 
        Bestscore = Minscore
        Bestmoves = Minmoves
    else:
        Bestscore = Maxscore
        Bestmoves = Maxmoves
    print(f"best move = {Bestmoves}\n score = {Bestscore} \nrepitions : {rep}")
    return(Bestmoves[0])
###########

#######################################################

board =[[" "," "," "],
        [" "," "," "],
        [" "," "," "]]
p = 1
turns = 0
while True:
    if turns == 9:
        print("Draw!")
        print(f"{board[0]}\n{board[1]}\n{board[2]}\n")
        quit()
    p =  not p
################################################## player turn ##################################################
    if p == 1:
        while True:
            player = "X"
            print("",board[0],"\n",board[1],"\n",board[2],"\n")
            col =int(input("input your collum 1-3:"))
            row =int(input("input your row 1-3:"))
            row -= 1
            col -= 1
            if board[row][col] == " ":
                board[row][col] = player
                if getwinner(board,player,row) == True:
                    print (f"{board[0]}\n{board[1]}\n{board[2]}\n You Win!")
                    quit()
                else:
                    break
            else:
                print("that spot is already taken")
################################################################################################################

################################################## robot turn ##################################################
    else:
        player = "O"
        copy_board = copy.deepcopy(board)
        if turns == 0:
            board[1][1] = "O"
        else:
            move = minmax2(copy_board)
            board[move[0]][move[1]] = player
            if getwinner(board,player,move[0]) == True:
                    print("",board[0],"\n",board[1],"\n",board[2],"\n")
                    print("player 0 wins")
                    break
################################################################################################################

    turns+=1