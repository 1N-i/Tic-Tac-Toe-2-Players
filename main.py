from game import make_move, table, verify_end_game, switch_player

player = "X"
for round in range(9):
    table()
    make_move(player)
    if verify_end_game(round) == True:
        print(f"Victory of '{player}'")
        table()
        break
    elif verify_end_game(round) == "Draw":
        print("Draw")
        table()
        break
    player = switch_player(player)