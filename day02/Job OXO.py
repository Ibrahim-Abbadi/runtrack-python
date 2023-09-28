import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 15
LINE_COLOR = (0, 0, 0)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe1337")

# Initialize the game grid
grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Function to draw the grid lines
def draw_grid():
    for row in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw X or O in a cell
def draw_move(row, col, player):
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2

    if player == 'X':
        pygame.draw.line(screen, X_COLOR, (x - 50, y - 50), (x + 50, y + 50), LINE_WIDTH)
        pygame.draw.line(screen, X_COLOR, (x + 50, y - 50), (x - 50, y + 50), LINE_WIDTH)
    else:
        pygame.draw.circle(screen, O_COLOR, (x, y), CELL_SIZE // 2 - 20, LINE_WIDTH)

# Function to check if there's a winner
def check_winner(player):
    # Check rows
    for row in grid:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(GRID_SIZE):
        if all(grid[row][col] == player for row in range(GRID_SIZE)):
            return True

    # Check diagonals
    if all(grid[i][i] == player for i in range(GRID_SIZE)) or all(grid[i][GRID_SIZE - i - 1] == player for i in range(GRID_SIZE)):
        return True

    return False

# Main game loop
current_player = 'X'
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            row = y // CELL_SIZE
            col = x // CELL_SIZE

            if grid[row][col] == '':
                grid[row][col] = current_player
                draw_move(row, col, current_player)
                if check_winner(current_player):
                    print(f"Player {current_player} wins!")
                    game_over = True
                elif all(cell != '' for row in grid for cell in row):
                    print("It's a draw!")
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    draw_grid()
    pygame.display.flip()
