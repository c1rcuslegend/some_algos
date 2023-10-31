# a function recieves a board 9*9, where "." is an empty cell and "1"-"9" are for digits
def solveSudoku(board):
    # checking for wich square does coordinate corresponds
    # and returning the interval
    def checks(k):
        if 0 <= k < 3:
            return [0, 1, 2]
        elif 3 <= k < 6:
            return [3, 4, 5]
        return [6, 7, 8]
    # checking if the number can be placed in such cell
    # by reviewing row, column and square not to have such number
    def push(i, j, val):
        # checking row and column
        for q in range(9):
            if board[q][j] == val or board[i][q] == val:
                return False
        # calling a function to find wich square do we need to check
        temp1, temp2 = checks(i), checks(j)
        # checking the square of cells
        for x in temp1:
            for y in temp2:
                if board[x][y] == val:
                    return False
        return True
    # main recursive function
    # the first argument is a row and the second one is a column
    def back(a, b):
        # return True if we have checked all the rows
        if a == 9:
            return True
        # start recursion from the next row if we have finished with all the columns
        if b == 9:
            return back(a + 1, 0)
        # cycle for each empty cell in a row
        for y in range(b, 9):
            # if the cell is empty
            if board[a][y] == ".":
                # checking every possible digit, wich can be placed
                for u in range(1, 10):
                    # continue if placing a digit is breaking the rules of sudoku
                    if not push(a, y, str(u)):
                        continue
                    board[a][y] = str(u)
                    # continue recursion with such digit placed in a cell
                    if back(a, y + 1):
                        # True if sudoku with such digit works out to be an answer
                        return True
                    # make the cell empty again if this digit didn't work out
                    board[a][y] = "."
                # return False if none of the digits works out, so we need to come back and change the previous ones
                return False
            else:
                # otherwise continue recursion from the next column in a row
                return back(a, b + 1)
    # call a function starting from the first row and column
    back(0, 0)

    return board
