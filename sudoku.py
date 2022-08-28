import numpy as np
sudoku = []
print("Please use 0 in place of blank spaces")
for i in range(9):
    row = list(input("Enter the elements of row {} without any space and commas: ".format(i+1)))
    row = [int(i) for i in row]
    sudoku.append(row)
print(np.matrix(sudoku))

def possible(x,y,n):
    global sudoku
    for i in range(0,9):
        if sudoku[y][i] == n:
            return False
    for i in range(0,9):
        if sudoku[i][x] == n:
            return False
    box_y = (y//3)*3
    box_x = (x//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[box_y+i][box_x+j]==n:
                return False
    return True
def solve():
    for y in range(0,9):
        for x in range(0,9):
            if sudoku[y][x] == 0:
                for n in range(1,10):
                    if possble(y,x,n):
                        sudoku[y][x] =n
                        solve()
                        sudoku[y][x] = n
                return
    print(np.matrix(sudoku))
    print("More???")
    solve()