import datetime


f = open("input2.txt", "r")
rows = int(f.readline())

final_board = []
# get all values in int
for i in range(rows):
    board = []
    line = f.readline()
    for values in range(rows):
        board.append(int(line[values]))

    final_board.insert(i, board)
f.close()






# copy an array without reference
def copy(original):
    a = 0

    final_copy = []
    for i in original:
        abc = []

        for c in i:
            abc.append(c)

        final_copy.insert(a, abc)
        a = a + 1
    return final_copy


# player moves value
playerAi = 1
opponentAi = 2


def changed_array(mod_board):
    modify_board = copy(mod_board)
    for i in range(len(modify_board)):
        for c in range(len(modify_board)):
            flag1 = 0
            flag2 = 0
            flag3 = 0
            flag4 = 0
            flag5 = 0
            flag6 = 0
            flag7 = 0
            flag8 = 0

            if modify_board[i][c] == 1:
                for a in range(1, 4):
                    if -1 < i + a < len(modify_board):
                        if modify_board[i + a][c] == 3:
                            flag1 = 1
                        if flag1 == 1:
                            pass
                        else:
                            if modify_board[i + a][c] == 5 or modify_board[i + a][c] == 6:
                                modify_board[i + a][c] = 6
                            else:
                                modify_board[i + a][c] = 4

                    if -1 < c + a < len(modify_board):
                        if modify_board[i][c + a] == 3:
                            flag2 = 1
                        if flag2 == 1:
                            pass
                        else:
                            if modify_board[i][c + a] == 5 or modify_board[i][c + a] == 6:
                                modify_board[i][c + a] = 6
                            else:
                                modify_board[i][c + a] = 4

                    if -1 < c + a < len(modify_board) and -1 < i + a < len(modify_board) :
                        if modify_board[i + a][c + a] == 3:
                            flag3 = 1
                        if flag3 == 1:
                            pass
                        else:
                            if modify_board[i + a][c + a] == 5 or modify_board[i + a][c + a] == 6:
                                modify_board[i + a][c + a] = 6
                            else:
                                modify_board[i + a][c + a] = 4

                    if -1 < c + a < len(modify_board) and -1 < i - a < len(modify_board):
                        if modify_board[i - a][c + a] == 3:
                            flag4 = 1
                        if flag4 == 1:
                            pass
                        else:
                            if modify_board[i - a][c + a] == 5 or modify_board[i - a][c + a] == 6:
                                modify_board[i - a][c + a] = 6
                            else:
                                modify_board[i - a][c + a] = 4
                for a in range(-1, -4,-1):
                    if -1 < i + a < len(modify_board) :
                        if modify_board[i + a][c] == 3:
                            flag5 = 1
                        if flag5 == 1:
                            pass
                        else:
                            if modify_board[i + a][c] == 5 or modify_board[i + a][c] == 6:
                                modify_board[i + a][c] = 6
                            else:
                                modify_board[i + a][c] = 4

                    if -1 < c + a < len(modify_board) :
                        if modify_board[i][c + a] == 3:
                            flag6 = 1
                        if flag6== 1:
                            pass
                        else:
                            if modify_board[i][c + a] == 5 or modify_board[i][c + a] == 6:
                                modify_board[i][c + a] = 6
                            else:
                                modify_board[i][c + a] = 4

                    if -1 < c + a < len(modify_board) and -1 < i + a < len(modify_board):
                        if modify_board[i + a][c + a] == 3:
                            flag7 = 1
                        if flag7== 1:
                            pass
                        else:
                            if modify_board[i + a][c + a] == 5 or modify_board[i + a][c + a] == 6:
                                modify_board[i + a][c + a] = 6
                            else:
                                modify_board[i + a][c + a] = 4

                    if -1 < c + a < len(modify_board) and -1 < i - a < len(modify_board):
                        if modify_board[i - a][c + a] == 3:
                            flag8 = 1
                        if flag8== 1:
                            pass
                        else:
                            if modify_board[i - a][c + a] == 5 or modify_board[i - a][c + a] == 6:
                                modify_board[i - a][c + a] = 6
                            else:
                                modify_board[i - a][c + a] = 4

            elif modify_board[i][c] == 2:
                for a in range(1, 4):
                    if -1 < i + a < len(modify_board):
                        if modify_board[i + a][c] == 3:
                            flag1 = 1
                        if flag1 == 1:
                            pass
                        else:
                            if modify_board[i + a][c] == 4 or modify_board[i + a][c] == 6:
                                modify_board[i + a][c] = 6
                            else:
                                modify_board[i + a][c] = 5

                    if -1 < c + a < len(modify_board):
                        if modify_board[i][c + a] == 3:
                            flag2 = 1
                        if flag2 == 1:
                            pass
                        else:
                            if modify_board[i][c + a] == 4 or modify_board[i][c + a] == 6:
                                modify_board[i][c + a] = 6
                            else:
                                modify_board[i][c + a] = 5

                    if -1 < c + a < len(modify_board) and -1 < i + a < len(modify_board) :
                        if modify_board[i + a][c + a] == 3:
                            flag3 = 1
                        if flag3 == 1:
                            pass
                        else:
                            if modify_board[i + a][c + a] == 4 or modify_board[i + a][c + a] == 6:
                                modify_board[i + a][c + a] = 6
                            else:
                                modify_board[i + a][c + a] = 5

                    if -1 < c + a < len(modify_board) and -1 < i - a < len(modify_board):
                        if modify_board[i - a][c + a] == 3:
                            flag4 = 1
                        if flag4 == 1:
                            pass
                        else:
                            if modify_board[i - a][c + a] == 4 or modify_board[i - a][c + a] == 6:
                                modify_board[i - a][c + a] = 6
                            else:
                                modify_board[i - a][c + a] = 5
                for a in range(-1, -4,-1):
                    if -1 < i + a < len(modify_board):
                        if modify_board[i + a][c] == 3:
                            flag5 = 1
                        if flag5 == 1:
                            pass
                        else:
                            if modify_board[i + a][c] == 4 or modify_board[i + a][c] == 6:
                                modify_board[i + a][c] = 6
                            else:
                                modify_board[i + a][c] = 5

                    if -1 < c + a < len(modify_board):
                        if modify_board[i][c + a] == 3:
                            flag6 = 1
                        if flag6 == 1:
                            pass
                        else:
                            if modify_board[i][c + a] == 4 or modify_board[i][c + a] == 6:
                                modify_board[i][c + a] = 6
                            else:
                                modify_board[i][c + a] = 5

                    if -1 < c + a < len(modify_board) and -1 < i + a < len(modify_board):
                        if modify_board[i + a][c + a] == 3:
                            flag7 = 1
                        if flag7 == 1:
                            pass
                        else:
                            if modify_board[i + a][c + a] == 4 or modify_board[i + a][c + a] == 6:
                                modify_board[i + a][c + a] = 6
                            else:
                                modify_board[i + a][c + a] = 5

                    if -1 < c + a < len(modify_board) and -1 < i - a < len(modify_board):
                        if modify_board[i - a][c + a] == 3:
                            flag8 = 1
                        if flag8 == 1:
                            pass
                        else:
                            if modify_board[i - a][c + a] == 4 or modify_board[i - a][c + a] == 6:
                                modify_board[i - a][c + a] = 6
                            else:
                                modify_board[i - a][c + a] = 5

    return modify_board


def get_score(final):
    player_score = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if final[i][j] == 1 or final[i][j] == 4 or final[i][j] == 6:
                player_score = player_score + 1
    return player_score





def getbestmove(initial):
        a=datetime.datetime.now()
        maxpoints = -10000
        # the output value
        next_move = {
            "row": -1,
            "column": -1,
        }
        initial = changed_array(initial)
        for i in range(len(initial)):
            for j in range(len(initial)):
                if initial[i][j] == 0:
                    initial[i][j] = 1
                    helper=changed_array(initial)
                    movepoints=minimax(helper,0,False,-10000,10000)

                    initial[i][j]=0

                    if(movepoints>maxpoints):
                        maxpoints=movepoints

                        next_move["row"]=i
                        next_move["column"]=j


                b = datetime.datetime.now()
                delta = b - a
                if int(delta.total_seconds())>55:
                    return next_move


        return next_move

def ismovesleft(board):
    for i in board:
        for c in i:
            if c==0:
                return True
            else:
                pass
    return False




def minimax(helper,depth,isplayer, alpha,beta):
    if depth == 3:
        if len(helper) <= 8:
            return get_score(helper)

    if depth == 2:
        if 9 <= len(helper):
            return get_score(helper)




    if not(ismovesleft(helper)):
        return get_score(helper)

    if isplayer==True:
        best=-10000

        for i in range(len(helper)):
            for j in range(len(helper)):
                if helper[i][j]==0:
                    helper[i][j]=1
                    test=changed_array(helper)
                    isplayer=False
                    best = max(best,minimax(test, depth + 1,  isplayer ,alpha,beta))
                    alpha = max(alpha, best)
                    helper[i][j]=0
                    if beta <= alpha:
                        break
        return best
    if  isplayer==False:
        best=10000

        for i in range(len(helper)):
            for j in range(len(helper)):
                if helper[i][j] == 0:
                    helper[i][j] = 2
                    test = changed_array(helper)
                    isplayer=True

                    best = min(best, minimax(test, depth + 1,  isplayer,alpha,beta))
                    beta = min(beta, best)

                    helper[i][j] = 0
                    if beta <= alpha:
                        break
        return best



bestestmove=getbestmove(final_board)
f = open("output.txt", "w")
f.write("%d %d" % (bestestmove["row"], bestestmove["column"]))
