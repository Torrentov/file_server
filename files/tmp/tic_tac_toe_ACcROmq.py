from tkinter import *


def move_0_0():
    global root
    root.destroy()
    global tic_tac_toe
    global human_player
    x = 0
    y = 0
    tic_tac_toe[x][y] = human_player
    if not(continue_game(tic_tac_toe)):
        createTable(tic_tac_toe)
    x, y = bot_move(tic_tac_toe, bot_player)
    tic_tac_toe[x][y] = bot_player
    createTable(tic_tac_toe)
    return None
    

def move_0_1():
    global root
    root.destroy()
    global tic_tac_toe
    global human_player
    x = 0
    y = 1
    tic_tac_toe[x][y] = human_player
    if not(continue_game(tic_tac_toe)):
        createTable(tic_tac_toe)
    x, y = bot_move(tic_tac_toe, bot_player)
    tic_tac_toe[x][y] = bot_player
    createTable(tic_tac_toe)
    return None


def move_0_2():
    global root
    root.destroy()
    global tic_tac_toe
    global human_player
    x = 0
    y = 2
    tic_tac_toe[x][y] = human_player
    if not(continue_game(tic_tac_toe)):
        createTable(tic_tac_toe)
    x, y = bot_move(tic_tac_toe, bot_player)
    tic_tac_toe[x][y] = bot_player
    createTable(tic_tac_toe)
    return None


def move_1_0():
    global root
    root.destroy()
    global tic_tac_toe
    global human_player
    x = 1
    y = 0
    tic_tac_toe[x][y] = human_player
    if not(continue_game(tic_tac_toe)):
        createTable(tic_tac_toe)
    x, y = bot_move(tic_tac_toe, bot_player)
    tic_tac_toe[x][y] = bot_player
    createTable(tic_tac_toe)
    return None


def move_1_1():
    global root
    root.destroy()
    global tic_tac_toe
    global human_player
    x = 1
    y = 1
    tic_tac_toe[x][y] = human_player
    if not(continue_game(tic_tac_toe)):
        createTable(tic_tac_toe)
    x, y = bot_move(tic_tac_toe, bot_player)
    tic_tac_toe[x][y] = bot_player
    createTable(tic_tac_toe)
    return None


def move_1_2():
    global root
    root.destroy()
    global tic_tac_toe
    global human_player
    x = 1
    y = 2
    tic_tac_toe[x][y] = human_player
    if not(continue_game(tic_tac_toe)):
        createTable(tic_tac_toe)
    x, y = bot_move(tic_tac_toe, bot_player)
    tic_tac_toe[x][y] = bot_player
    createTable(tic_tac_toe)
    return None


def move_2_0():
    global root
    root.destroy()
    global tic_tac_toe
    global human_player
    x = 2
    y = 0
    tic_tac_toe[x][y] = human_player
    if not(continue_game(tic_tac_toe)):
        createTable(tic_tac_toe)
    x, y = bot_move(tic_tac_toe, bot_player)
    tic_tac_toe[x][y] = bot_player
    createTable(tic_tac_toe)
    return None


def move_2_1():
    global root
    root.destroy()
    global tic_tac_toe
    global human_player
    x = 2
    y = 1
    tic_tac_toe[x][y] = human_player
    if not(continue_game(tic_tac_toe)):
        createTable(tic_tac_toe)
    x, y = bot_move(tic_tac_toe, bot_player)
    tic_tac_toe[x][y] = bot_player
    createTable(tic_tac_toe)
    return None


def move_2_2():
    global root
    root.destroy()
    global tic_tac_toe
    global human_player
    x = 2
    y = 2
    tic_tac_toe[x][y] = human_player
    if not(continue_game(tic_tac_toe)):
        createTable(tic_tac_toe)
    x, y = bot_move(tic_tac_toe, bot_player)
    tic_tac_toe[x][y] = bot_player
    createTable(tic_tac_toe)
    return None


def player_detect_cross():
    global root
    root.destroy()
    global human_player
    global bot_player
    human_player = "Cross"
    bot_player = "Zero"
    single_player()
    return None


def player_detect_zero():
    global root
    root.destroy()
    global human_player
    global bot_player
    human_player = "Zero"
    bot_player = "Cross"
    single_player()
    return None


def one_player_mode():
    global root
    global players
    root.destroy()
    players = 1
    root = Tk()
    canv = Canvas(width=500, height=500, bg="beige")
    btn_Cross = Button(root, text="Play for cross", font="Verdana 20", bg="beige", command=player_detect_cross).place(x=150, y=190, width=200, height=30)
    btn_Zero = Button(root, text="Play for zero", font="Verdana 20", bg="beige", command=player_detect_zero).place(x=150, y=220, width=200, height=30)
    canv.pack()
    root.mainloop()


def two_player_mode():
    global players
    global root
    root.destroy()
    players = 2
    global tic_tac_toe
    global human_player
    human_player = "Zero"
    createTable(tic_tac_toe)

            
def single_player():
    global tic_tac_toe
    global bot_player
    global human_player
    player = "Cross"
    if player == human_player:
        createTable(tic_tac_toe)
    else:
        current_board = []
        for elem in tic_tac_toe:
            current_board.append(elem[:])
        x, y = bot_move(current_board, bot_player)
        tic_tac_toe[x][y] = bot_player
        isFinal = createTable(tic_tac_toe)
        if isFinal == 1:
            sys.exit()


winning_move = [-1, -1]


def defense_check(wins):
    global tic_tac_toe
    global winning_move
    final = []
    for i in range(len(wins)):
        elem = wins[i]
        board = []
        for line in tic_tac_toe:
            board.append(line[:])
        x = elem[2]
        y = elem[3]
        board[x][y] = human_player
        if bot_check(board) == human_player:
            final.append(elem[:])
        board[x][y] = bot_player
        if bot_check(board) == bot_player:
            winning_move = [x, y]
            return []
    return final


def bot_check(tic_tac_toe):
    if (tic_tac_toe[0][0] == tic_tac_toe[1][1]) and (tic_tac_toe[0][0] == tic_tac_toe[2][2]) and (tic_tac_toe[0][0] != 0):
        return tic_tac_toe[0][0]
    elif (tic_tac_toe[0][2] == tic_tac_toe[1][1]) and (tic_tac_toe[0][2] == tic_tac_toe[2][0]) and (tic_tac_toe[1][1] != 0):
        return tic_tac_toe[1][1]
    else:
        for i in range(3):
            if (tic_tac_toe[i][0] == tic_tac_toe[i][1]) and (tic_tac_toe[i][0] == tic_tac_toe[i][2]) and (tic_tac_toe[i][0] != 0):
                return tic_tac_toe[i][0]
            elif (tic_tac_toe[0][i] == tic_tac_toe[1][i]) and (tic_tac_toe[0][i] == tic_tac_toe[2][i]) and (tic_tac_toe[0][i] != 0):               
                return tic_tac_toe[0][i]
    return 0


layer = 0


def chance(board, player):
    global player_wins
    global pc_wins
    global draws
    global layer
    global bot_player
    global human_player
    layer += 1
    current_table = []
    for elem in board:
        current_table.append(elem[:])
    for i in range(3):
        for j in range(3):
            if current_table[i][j] == 0:
                current_table[i][j] = player
                if bot_check(current_table) == bot_player:
                    pc_wins += 1
                    layer -= 1
                    return None
                elif bot_check(current_table) == human_player:
                    player_wins += 1
                    layer -= 1
                    return None
                else:
                    if player == bot_player:
                        chance(current_table, human_player)
                    else:
                        chance(current_table, bot_player)
    draws += 1
    layer -= 1
    return None
    

def bot_move(table, player):
    global bot_player
    global player_wins
    global pc_wins
    global layer
    global draws
    global winning_move
    global n
    wins = []
    for i in range(3):
        for j in range(3):
            bot_board = []
            for elem in table:
                bot_board.append(elem[:])
            if bot_board[i][j] == 0:
                bot_board[i][j] = player
                player_wins = 0
                pc_wins = 0
                draws = 0
                layer = 0
                if player == bot_player:
                    chance(bot_board, human_player)
                    wins.append([player_wins, pc_wins, i, j])
                    layer = 0
                    pc_wins = 0
                    draws = 0
                    player_wins = 0
                else:
                    chance(bot_board, bot_player)
                    wins.append([player_wins, pc_wins, i, j])
                    layer = 0
                    pc_wins = 0
                    draws = 0
                    player_wins = 0
    if wins == []:
        n = 1
        createTable(tic_tac_toe)
    else:
        massive = defense_check(wins)[:]
        if massive != []:
            wins = massive[:]
            minimum_pwins = wins[0][0]
            maximum_pcwins = wins[0][1]
            for elem in wins:
                if minimum_pwins > elem[0]:
                    best_move = [elem[2], elem[3]]
                    minimum_pwins = elem[0]
                elif minimum_pwins == elem[0]:
                    if maximum_pcwins <= elem[1]:
                        best_move = [elem[2], elem[3]]
                    break
        elif winning_move != [-1, -1]:
            best_move = [winning_move[0], winning_move[1]]
        else:
            minimum_pwins = wins[0][0]
            maximum_pcwins = wins[0][1]
            for elem in wins:
                if minimum_pwins > elem[0]:
                    best_move = [elem[2], elem[3]]
                    minimum_pwins = elem[0]
                elif minimum_pwins == elem[0]:
                    if maximum_pcwins <= elem[1]:
                        best_move = [elem[2], elem[3]]
                    break
        return best_move


def createTable(tic_tac_toe):
    global root
    global players
    global human_player
    if players == 2:
        if human_player == "Cross":
            human_player = "Zero"
        else:
            human_player = "Cross"
    n = 0
    root = Tk()
    canv = Canvas(root, width=500, height=500, bg="beige")
    canv.create_line(200, 100, 200, 400, width=5)
    canv.create_line(300, 100, 300, 400, width=5)
    canv.create_line(100, 200, 400, 200, width=5)
    canv.create_line(100, 300, 400, 300, width=5)
    if not(continue_game(tic_tac_toe)) == 1:
        n = 1
    for i in range(3):
        for j in range(3):
            if tic_tac_toe[i][j] == "Cross":
                x = (i + 1) * 100 + 15
                y = (j + 1) * 100 + 15
                canv.create_line(x, y, x + 70, y + 70, width=3)
                y += 70
                canv.create_line(x, y, x + 70, y - 70, width=3)
            elif tic_tac_toe[i][j] == "Zero":
                x = (i + 1) * 100 + 15
                y = (j + 1) * 100 + 15
                canv.create_oval(x, y, x + 70, y + 70, width=3)
            else:
                if n == 0:
                    x1 = (i + 1) * 100 + 2
                    y1 = (j + 1) * 100 + 2
                    if i == 0:
                        if j == 0:
                            btn_0_0 = Button(root, command=move_0_0, bg="beige").place(x=x1, y=y1, width=97.5, height=97.5)
                        elif j == 1:
                            btn_0_1 = Button(root, command=move_0_1, bg="beige").place(x=x1, y=y1, width=97.5, height=97.5)
                        else:
                            btn_0_2 = Button(root, command=move_0_2, bg="beige").place(x=x1, y=y1, width=97.5, height=97.5)
                    elif i == 1:
                        if j == 0:
                            btn_1_0 = Button(root, command=move_1_0, bg="beige").place(x=x1, y=y1, width=97.5, height=97.5)
                        elif j == 1:
                            btn_1_1 = Button(root, command=move_1_1, bg="beige").place(x=x1, y=y1, width=97.5, height=97.5)
                        else:
                            btn_1_2 = Button(root, command=move_1_2, bg="beige").place(x=x1, y=y1, width=97.5, height=97.5)
                    else:
                        if j == 0:
                            btn_2_0 = Button(root, command=move_2_0, bg="beige").place(x=x1, y=y1, width=97.5, height=97.5)
                        elif j == 1:
                            btn_2_1 = Button(root, command=move_2_1, bg="beige").place(x=x1, y=y1, width=97.5, height=97.5)
                        else:
                            btn_2_2 = Button(root, command=move_2_2, bg="beige").place(x=x1, y=y1, width=97.5, height=97.5)   
    if n == 1:
        check_win(tic_tac_toe, canv)
    canv.pack()
    root.mainloop()
    if n == 1:
        sys.exit()
    else:
        return 0


def move():
    if tic_tac_toe[x][y] == 0:
        tic_tac_toe[x][y] = player
        return tic_tac_toe
    else:
        print("Incorrect move, try again")
        return -1


def check_win(tic_tac_toe, canv):
    isit = 0
    if (tic_tac_toe[0][0] == tic_tac_toe[1][1]) and (tic_tac_toe[0][0] == tic_tac_toe[2][2]) and (tic_tac_toe[0][0] != 0):
        canv.create_text(250,250,text=tic_tac_toe[1][1] + " wins", font="Verdana 70", justify=CENTER,fill="red") 
        return 1
    elif (tic_tac_toe[0][2] == tic_tac_toe[1][1]) and (tic_tac_toe[0][2] == tic_tac_toe[2][0]) and (tic_tac_toe[1][1] != 0):
        canv.create_text(250,250,text=tic_tac_toe[1][1] + " wins", font="Verdana 70", justify=CENTER,fill="red") 
        return 1
    else:
        for i in range(3):
            if (tic_tac_toe[i][0] == tic_tac_toe[i][1]) and (tic_tac_toe[i][0] == tic_tac_toe[i][2]) and (tic_tac_toe[i][0] != 0):
                canv.create_text(250,250,text=tic_tac_toe[i][0] + " wins", font="Verdana 70", justify=CENTER,fill="red") 
                return 1
            elif (tic_tac_toe[0][i] == tic_tac_toe[1][i]) and (tic_tac_toe[0][i] == tic_tac_toe[2][i]) and (tic_tac_toe[0][i] != 0):
                canv.create_text(250,250,text=tic_tac_toe[0][i] + " wins", font="Verdana 70", justify=CENTER,fill="red")                 
                return 1
    for i in range(3):
        for j in range(3):
            if tic_tac_toe[i][j] == 0:
                isit = 1
                break
    if isit == 0:
        canv.create_text(250, 250, text="Draw", font="Verdana 120", justify=CENTER, fill="red")
        return 1
    return 0


def continue_game(tic_tac_toe):
    isit = 0
    if (tic_tac_toe[0][0] == tic_tac_toe[1][1]) and (tic_tac_toe[0][0] == tic_tac_toe[2][2]) and (tic_tac_toe[0][0] != 0):
        return False
    elif (tic_tac_toe[0][2] == tic_tac_toe[1][1]) and (tic_tac_toe[0][2] == tic_tac_toe[2][0]) and (tic_tac_toe[1][1] != 0):
        return False
    else:
        for i in range(3):
            if (tic_tac_toe[i][0] == tic_tac_toe[i][1]) and (tic_tac_toe[i][0] == tic_tac_toe[i][2]) and (tic_tac_toe[i][0] != 0):
                return False
            elif (tic_tac_toe[0][i] == tic_tac_toe[1][i]) and (tic_tac_toe[0][i] == tic_tac_toe[2][i]) and (tic_tac_toe[0][i] != 0):
                return False
    for i in range(3):
        for j in range(3):
            if tic_tac_toe[i][j] == 0:
                isit = 1
                break
    if isit == 0:
        return False
    return True


bot_player = 0
human_player = 0
player_wins = 0
pc_wins = 0
draws = 0
tic_tac_toe = [[0 for i in range(3)] for i in range(3)]

players = 0
buttons = []
root = Tk()
canv = Canvas(width=500, height=500, bg="beige")
btn_bot = Button(root, text = "Play with bot", font="Verdana 20", bg="beige", command=one_player_mode).place(x=150, y=190, width=220, height=30)
btn_2_player = Button(root, text="Play with friend", font="Verdana 20", bg="beige", command=two_player_mode).place(x=150, y=220, width=220, height=30)
canv.pack()
root.mainloop()