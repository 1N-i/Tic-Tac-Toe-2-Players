position = list(range(1, 10))

def make_move(player):
    while True: #Verify if the move is valid
        try:
            move = int(input(f"Play of '{player}': ")); print()
            if move not in position:
                raise ValueError
            position[move-1] = player
            break
        except ValueError:
            print("Invalid move")

def table(): #Show the game
    for e in range(9):
        if e == 2 or e == 5 or e == 8:
            print(f" {position[e]} ", end=" ")
            print()
            if e != 8:
                print("---|---|---")
        else:
            print(f" {position[e]} ", end="|")

def verify_end_game(round): #All options of a winner or a draw
    if position[0] == position[1] == position[2] or \
    position[3] == position[4] == position[5] or \
    position[6] == position[7] == position[8] or \
    position[0] == position[3] == position[6] or \
    position[1] == position[4] == position[7] or \
    position[2] == position[5] == position[8] or \
    position[0] == position[4] == position[8] or \
    position[2] == position[4] == position[6]:
        return True
    elif round == 8:
        return True
    
def switch_player(player): #Switch the player
    if player == "X":
        return "O"
    elif player == "O":
        return "X"