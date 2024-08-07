import random

def computer_move(board):
  available_moves = [i for i, spot in enumerate(board) if spot == " "]
  return random.choice(available_moves)

def player_move(board):
  while True:
    try:
      move = int(input("Enter a number (1-9) to make your move: "))
      if 0 < move < 10 and board[move - 1] == " ":
        return move - 1
      else:
        print("Invalid move. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def display_board(board):
  print("-------------")
  for i in range(0, 9, 3):
    print("| {} | {} | {} |".format(board[i], board[i+1], board[i+2]))
    print("-------------")

def check_win(board):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != " ":
      return board[condition[0]]
  return None

def play_game():
  board = [" " for _ in range(9)]
  current_player = "X"
  game_over = False

  while not game_over:
    display_board(board)

    if current_player == "X":
      move = player_move(board)
    else:
      move = computer_move(board)
      print("The computer played at position", move + 1)

    board[move] = current_player

    winner = check_win(board)
    if winner:
      display_board(board)
      print(f"{winner} wins!")
      game_over = True
    elif " " not in board:
      display_board(board)
      print("It's a tie!")
      game_over = True
    else:
      current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  play_game()