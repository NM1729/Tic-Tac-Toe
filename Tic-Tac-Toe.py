X="X"
O="O"

def introduce_game():
    """Introduce the game."""
    print("""
Welcome to the TIC-TAC-TOE game.
You know the rules. Let's play.
""")
def choose_players():
    """Choose the players."""
    #first ask player whether to play first or not
    #if yes, assign player the constant X
    #if no, assign computer the constant X
    choice = input("Do you want to go first(y/n)?").lower()
    while choice not in ("y","n"):
        choice = input("Invalid. Do you want to go first(y/n)?").lower()
    if choice == "y":
        player = X
        computer = O
    else:
        player = O
        computer = X
    return player, computer
def initialise_board():
    """Initialise the board"""
    board = [0,1,2,3,4,5,6,7,8]
    return board
def valid_moves(board):
    """Set the valid moves"""
    valid=[]
    for i in range(9):
        if board[i] not in ("X","O"):
            valid.append(i)
    return valid
def draw_board(board):
    """Draw the board"""
    print("\n\t",board[0],"|",board[1],"|",board[2])
    print("\t",board[3],"|",board[4],"|",board[5])
    print("\t",board[6],"|",board[7],"|",board[8])
def player_input(valid):
    """Receives input from player"""
    move=int(input("Make your move:"))
    while move not in valid:
        move=int(input("Make your move:"))
    return move
def computer_input(valid, board, player, computer):
    """Receives input from computer"""
    board=board[:]
    #If computer can win this turn, play the move
    for move in valid:
        board[move]=computer
        winner=check_winner(board)
        if(winner==computer):
            return move
        board[move]=move
    #If player can win next turn, play the move
    for move in valid:
        board[move]=player
        winner=check_winner(board)
        if(winner==player):
            return move
        board[move]=move
    move=valid[random.randrange(len(valid))]
    return move
def check_winner(board):
    """checks who won or lost"""
    WIN_TYPES=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in WIN_TYPES:
        if board[i[0]]==board[i[1]]==board[i[2]]!="":
            return board[i[0]]
    for number in (0,1,2,3,4,5,6,7,8):
        if number in board:
            return None
    return "TIE"
def reveal_winner(winner, player, computer, board):
    """reveals the winner"""
    draw_board(board)
    if winner == player:
        print("The player has won the game.\n")
    elif winner == computer:
        print("The computer has won the game.\n")
    elif winner == "TIE":
        print("The game is a tie.\n")
    else:
        print("Invalid result.\n")
def main():
    #introduce the game
    #choose players
    #initialise board
    #initialise winner
    #while winner not anyone or tie
    #display board
    #set valid moves
    #receive player input
    #receive computer input
    #check for winner
    #if no winner switch player
    #repeat above steps
    #if winner congratulate the winner
    introduce_game()
    player, computer = choose_players()
    turn = X
    board = initialise_board()
    winner = None
    while winner==None:
        valid = valid_moves(board)
        draw_board(board)
        if turn==player:
            move = player_input(valid)
            board[move]=player
        elif turn==computer:
            move = computer_input(valid, board, player, computer)
            board[move]=computer
        winner = check_winner(board)
        if winner == None:
            if turn == X:
               turn = O
            else:
               turn = X
    reveal_winner(winner, player, computer, board)

import random

main()

print("\n\nPress the enter key to continue.\n");
        
