import random
import os
import sys

def initialize_grid():
    grid = [[0] * 4 for _ in range(4)]
    add_new_tile(grid)
    add_new_tile(grid)
    return grid

def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])
        
def compress(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                pos += 1
    return new_grid

def merge(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
    return grid

def reverse(grid):
    new_grid = []
    for i in range(4):
        new_grid.append(list(reversed(grid[i])))
    return new_grid

def transpose(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([grid[j][i] for j in range(4)])
    return new_grid

def move_left(grid):
    grid = compress(grid)
    grid = merge(grid)
    grid = compress(grid)
    return grid

def move_right(grid):
    grid = reverse(grid)
    grid = move_left(grid)
    grid = reverse(grid)
    return grid

def move_up(grid):
    grid = transpose(grid)
    grid = move_left(grid)
    grid = transpose(grid)
    return grid

def move_down(grid):
    grid = transpose(grid)
    grid = move_right(grid)
    grid = transpose(grid)
    return grid

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print('\t'.join(str(num).ljust(4) for num in row))
    print()

def check_game_over(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
    return True

def main():
    grid = initialize_grid()
    
    while True:
        print_grid(grid)
        
        move = input("Press r/l/t/d to move or Q to quit: ").lower()
        
        if move == 't':
            grid = move_up(grid)
        elif move == 'l':
            grid = move_left(grid)
        elif move == 'd':
            grid = move_down(grid)
        elif move == 'r':
            grid = move_right(grid)
        elif move == 'q':
            print("Game over! Exiting...")
            sys.exit()

        add_new_tile(grid)
        
        if check_game_over(grid):
            print_grid(grid)
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
