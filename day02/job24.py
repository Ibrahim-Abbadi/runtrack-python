import random

class AI_One:
    def __init__(self):
        self.name = "AI_One"
        
    # "think" method
    def think(self, board, player_color):
        available_columns = [col for col in range(len(board[0])) if board[0][col] == ' ']

        # Winning move for the AI
        for col in available_columns:
            temp_board = [row[:] for row in board]
            self.make_move(temp_board, col, player_color)
            if self.is_winning_move(temp_board, player_color):
                return col

        # block winning move for the opponent
        opponent_color = 'red' if player_color == 'yellow' else 'yellow'
        for col in available_columns:
            temp_board = [row[:] for row in board]
            self.make_move(temp_board, col, opponent_color)
            if self.is_winning_move(temp_board, opponent_color):
                return col

        # Choose a random available column if there is no winning move
        return random.choice(available_columns)

    def make_move(self, board, col, player_color):
        for row in range(len(board) - 1, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = player_color
                break

    def is_winning_move(self, board, player_color):
        for row in range(len(board)):
            for col in range(len(board[0]) - 3):
                if all(board[row][col + i] == player_color for i in range(4)):
                    return True

        for col in range(len(board[0])):
            for row in range(len(board) - 3):
                if all(board[row + i][col] == player_color for i in range(4)):
                    return True

        for row in range(len(board) - 3):
            for col in range(len(board[0]) - 3):
                if all(board[row + i][col + i] == player_color for i in range(4)):
                    return True

        for row in range(3, len(board)):
            for col in range(len(board[0]) - 3):
                if all(board[row - i][col + i] == player_color for i in range(4)):
                    return True

        return False

# Test
def play_game():
    board = [[' ' for _ in range(7)] for _ in range(6)]
    ai = AI_One()

    while True:
        # Player's turn
        print("Current Board:")
        for row in board:
            print(' | '.join(row))
            print('-' * 21)
        player_col = int(input("Enter the column from 0 to 6: "))
        ai.make_move(board, player_col, 'red')
        if ai.is_winning_move(board, 'red'):
            print("Player wins!")
            break

        # AI's turn
        ai_col = ai.think(board, 'yellow')
        print(f"AI_One chooses column {ai_col}")
        ai.make_move(board, ai_col, 'yellow')
        if ai.is_winning_move(board, 'yellow'):
            print("AI_One wins!")
            break

if __name__ == "__main__":
    play_game()
