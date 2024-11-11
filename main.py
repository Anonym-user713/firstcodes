#Program is written on PyCharm
def tic_tac_toe():
    grid = [["*" for _ in range(3)] for _ in range(3)]

    player1 = input("Input your name player 1: ")
    player2 = input("Input your name player 2: ")

    is_player1_turn = True

    def check_win(symbol):
        for i in range(3):
            if all(grid[i][j] == symbol for j in range(3)) or all(grid[j][i] == symbol for j in range(3)):
                return True
        if grid[0][0] == grid[1][1] == grid[2][2] == symbol or grid[0][2] == grid[1][1] == grid[2][0] == symbol:
            return True
        return False

    while True:
        current_player = player1 if is_player1_turn else player2
        current_symbol = 'x' if is_player1_turn else 'o'

        try:
            row, col = map(int, input(
                f"Your turn {current_player}, enter coordinates where you want to move (row, col): ").split(","))

            if grid[row - 1][col - 1] == "*":
                grid[row - 1][col - 1] = current_symbol
            else:
                print("This field is already taken.")
                continue
        except (ValueError, IndexError):
            print("Wrong input. Try again.")
            continue

        separator = "-" * (len(grid[0]) * 2 + 1)
        for i in range(len(grid)):
            print(separator)
            print("|", end="")
            for o in range(len(grid[i])):
                print(grid[i][o], end="|")
            print()
        print(separator)

        if check_win(current_symbol):
            print(f"Congratulations {current_player}! You have won the game.")
            break

        is_player1_turn = not is_player1_turn

        if all(grid[i][j] != "*" for i in range(3) for j in range(3)):
            print("It's a tie!")
            break

while True:
   tic_tac_toe()
   again = input("Do you want to play again (y or n)? ")
   if again in ("yes", "y", "Yes", "Y"):
      continue
   elif again in ("No","N","no","n"):
      break
   else:
      print("Wrong input")
      break