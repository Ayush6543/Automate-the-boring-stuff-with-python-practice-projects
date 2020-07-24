grid_lines = [['.', '.', '.', '.', '.', '.'],
              ['.', 'O', 'O', '.', '.', '.'],
              ['O', 'O', 'O', 'O', '.', '.'],
              ['O', 'O', 'O', 'O', 'O', '.'],
              ['.', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', '.'],
              ['O', 'O', 'O', 'O', '.', '.'],
              ['.', 'O', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.']]


def grid_line(grid):
    for i in range(len(grid[0])):
        for grid_lining in grid:
            print(grid_lining[i], end="")
        print()


grid_line(grid_lines)
