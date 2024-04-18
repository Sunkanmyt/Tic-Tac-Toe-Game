from random import randrange

def display_board(board):
    for row in range(3):
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        
        for col in range(3):
           print(f"|   {board[row][col]}   ", end = "")
    
        print("|")   
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")


def enter_move(board):
    ok = True
    while ok:
        move = int(input("Enter a move: "))

        if move < 1 or move > 9:
            print("Enter a valid input!")
            continue
        
        loc = move - 1
        row = loc // 3
        col = loc % 3
        
        if board[row][col] not in ["O", "X"]:
           board[row][col] = "O"
           ok = False
        else:
            print("Slot is filled")
            continue


def make_list_of_free_fields(board):
    free = []
    
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["O", "X"]:
                free.append((row,col))
    
    return free


def victory_for(board, sign):
    if sign == "O":
        who = "You"
    elif sign == "X":
        who = "Me"
    else:
        who = None

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return who
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return who
   
    for rc in range(3):
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return who
        elif board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return who

    return None


def draw_move(board):
	free = make_list_of_free_fields(board) # make a list of free fields
	cnt = len(free)
	if cnt > 0:	
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = "X"
display_board(board)
    
slots = make_list_of_free_fields(board)
my_move = True 

while len(slots) > 0:
    if my_move:
        enter_move(board)
        victor = victory_for(board, "O")
    else:
        draw_move(board)
        victor = victory_for(board, "X")

    display_board(board)    
    if victor != None:
        break

    my_move = not my_move
    slots = make_list_of_free_fields(board)
    
if victor == "You":
    print("You won!")
elif victor == "Me":
    print("I won!")
else:
    print("It's a Tie!")
