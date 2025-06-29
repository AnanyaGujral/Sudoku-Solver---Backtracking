def valid_move(my_grid, row, col, num):
    for x in range(9):
        if my_grid[row][x] == num:
            return False
        
    for x in range(9):
        if my_grid[x][col] == num:
            return False
        
    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if my_grid[corner_row + x][corner_col + y] == num:
                return False
        
    return True

def solver(my_grid, row, col):

    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if my_grid[row][col] > 0:
        return solver(my_grid, row, col + 1)
    
    for num in range(1, 10):
        if valid_move(my_grid, row, col, num):
            my_grid[row][col] = num
            if solver(my_grid, row, col + 1):
                return True
            
        my_grid[row][col] = 0

    return False

my_grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

if solver(my_grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(my_grid[i][j], end=" ")
        print()
else:
    print("There are no solutions for this Sudoku:(")