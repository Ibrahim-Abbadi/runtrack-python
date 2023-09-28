def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'X':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'X':
            return False


    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'X':
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        for row in board:
            print(' '.join(row))
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'X'
            solve_n_queens(board, row + 1, n)
            board[row][col] = 'O'  # Backtrack

def main():
    n = int(input("Enter the value of n : "))
    board = [['O' for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)

if __name__ == "__main__":
    main()
