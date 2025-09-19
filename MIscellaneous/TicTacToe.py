import random
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    border = "+-------+-------+-------+"
    inside = "|       |       |       |"
    print(border)
    print(inside)
    print("|   "+ board[0] +"   |   "  + board[1] + "   |   " + board[2] +"   |")
    print(inside)
    print(border)
    print(inside)
    print("|   "+ board[3] +"   |   "  + board[4] + "   |   " + board[5] +"   |")
    print(inside)
    print(border)
    print(inside)
    print("|   "+ board[6]+"   |   "  + board[7] + "   |   " + board[8] +"   |")
    print(inside)
    print(border)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    Not_moved = True
    while Not_moved:
        index = int(input("Enter your move: "))
    
        if index < 10 and index > 0:
            if board[index-1] == "X":
                print("I made the move already. Pick another move.")
            elif board[index-1] == "O":
                print("You made the move already. Pick another move.")
            else:
                board[index-1] = "O"
                Not_moved == False
                return board
        else:
            print("Enter a number from 1 to 10")
            
def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0] == sign and board[1] == sign and board[2] == sign:
        return True
    elif board[3] == sign and board[4] == sign and board[5] == sign:
        return True
    elif board[6] == sign and board[7] == sign and board[8] == sign:
        return True
    elif board[0] == sign and board[3] == sign and board[6] == sign:
        return True
    elif board[1] == sign and board[4] == sign and board[7] == sign:
        return True
    elif board[2] == sign and board[5] == sign and board[8] == sign:
        return True
    elif board[0] == sign and board[4] == sign and board[8] == sign:
        return True
    elif board[2] == sign and board[4] == sign and board[6] == sign:
        return True
    else:
        return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    checkboard = []
    for n in board:
        if n != "X" and n != "O":
            checkboard.append(board[int(n)-1])
    print(checkboard)
   
    index = random.randint(0,len(checkboard)-1)
    print("My move is ", checkboard[index])
    board[int(checkboard[index])-1] = "X"
    return board


newboard = ['1','2','3','4','5','6','7','8','9'] 
display_board(newboard)
print("I start first. X in the middle.")
newboard[4] = "X"

for count in range(1,5):
    display_board(newboard)
    newboard = enter_move(newboard)
    Victory = victory_for(newboard, "O")
    if(Victory):
        print("CONGRATS PLAYER. You Won!")
        break
    display_board(newboard)
    newboard = draw_move(newboard)
    Victory = victory_for(newboard, "X")
    if(Victory):
        print("Game Over!")
        break
print("No more moves!")