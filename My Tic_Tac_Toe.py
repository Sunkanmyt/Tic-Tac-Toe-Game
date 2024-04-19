from random import randrange

# Create a function to display the current state of the board
def display_board(board):
    for row in range(3):
        print("+-------" * 3 + "+") 
        print("|       " * 3 + "|")
        
        for col in range(3):
           print(f"|   {board[row][col]}   ", end = "") # Get the values from the 2D board list
    
        print("|")   
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")


# Create a function to allow player enter a move
def enter_move(board):
    ok = True # A 
    while ok:
        move = int(input("Enter a move: ")) # Get the value from the user and convert to the integer data type

        if move < 1 or move > 9: # Test the validity of the user's input
            print("Enter a valid input!") 
            continue
        
        loc = move - 1 # Get the actual index of the user's input since indexing starts from 0
        row = loc // 3 # Get the row it falls in.
        col = loc % 3 # Get the column it falls in.
        
        if board[row][col] not in ["O", "X"]: # Check if the field is filled already
           board[row][col] = "O"
           ok = False
        else:
            print("Field is occupied, choose another field.") # Print this in the event that the field if occupied
            continue


# Create a function to make a list of available fields on the board
def make_list_of_free_fields(board):
    free = [] # Create an empty list
    
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["O", "X"]: # Check that the field is not yet occupied
                free.append((row,col)) # Append the index of the row and column of the field as a tuple in the format => (row, col) to the "free" list
    
    return free # Return the list of free fields on the board


# Create a function to check if any player has won the game
def victory_for(board, sign):
    # Check the sign passed into the function and assign values appropriately
    if sign == "O":
        who = "You"
    elif sign == "X":
        who = "Me"
    else:
        who = None

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign: # To check the first diagonal
        return who
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign: # To check the second diagonal
        return who
   
    for rc in range(3):
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign: # To the check the columns
            return who
        elif board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign: # To check the rows
            return who

    return None # Return a "None" value in the event that no winner emerges


# Create a function to allow the computer program make a move
def draw_move(board):
	free = make_list_of_free_fields(board) # Make a list of free fields using the previous function created
	cnt = len(free) # Get how many free fields are availble
	if cnt > 0:	
		this = randrange(cnt) # Use the randrange function to generate random numbers less that the value passed into the function and store it as an index
		row, col = free[this] # Using the index chosen randomly, assign the row and column values from the corresponding tuple in the "free" list
		board[row][col] = 'X' # Update the field



# Create a 2D list using the appropriate syntax
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)] 
board[1][1] = "X" # Allow the computer program make the first move at the center
display_board(board)
    
fields = make_list_of_free_fields(board) # Get the list of available fields
my_move = True 

# Alternate the play
while len(fields) > 0:
    if my_move: # This runs when the user's move (my_move) is True
        enter_move(board) # The user enters a move
        victor = victory_for(board, "O") # Checks for victory
    else:
        draw_move(board) # Computer enters a move
        victor = victory_for(board, "X") # Checks for victory

    display_board(board)    
    if victor != None: 
        break # In the event that a victor emerges, the loop is terminated

    my_move = not my_move
    fields = make_list_of_free_fields(board) # Available fields are updated

# Print the appropriate message based on the value of the "victor" variable
if victor == "You":
    print("You won!")
elif victor == "Me":
    print("I won!")
else:
    print("It's a Tie!")
