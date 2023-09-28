class Connect4:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [['O' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 'R'

    def play(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == 'O':
                self.board[row][col] = self.current_player
                return True
        return False

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print('-' * (self.cols * 2 - 1))
        print(' '.join(str(i) for i in range(self.cols)))

    def check_winner(self):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != 'O':
                    for dr, dc in directions:
                        for _ in range(4):
                            r, c = row + dr * _, col + dc * _
                            if not (0 <= r < self.rows and 0 <= c < self.cols) or self.board[r][c] != self.current_player:
                                break
                        else:
                            return True
        return False

    def switch_player(self):
        self.current_player = 'J' if self.current_player == 'R' else 'R'

    def play_game(self):
        while True:
            self.print_board()
            col = int(input(f"Player {self.current_player}, choose a column (0-{self.cols - 1}): "))
            if 0 <= col < self.cols:
                if self.play(col):
                    if self.check_winner():
                        self.print_board()
                        print(f"Player {self.current_player} wins!")
                        return
                    self.switch_player()
                else:
                    print("Column is full")
            else:
                print("Invalid column")

if __name__ == "__main__":
    game = Connect4()
    game.play_game()
