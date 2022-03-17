# Sudoku Solver Using Recursion and Backtracking
# kushal das
# 17/3/2022

def find_next_empty(puzzle):
    """
    Finds the next empty row or column that is not yet filled
    :param puzzle:
    :return:tuple(row,col) or (None,None) if no more space
    """
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c  # if rth row and cth col is empty then return that row and column
    return None, None  # if there are no more space left then we return None,None


def is_valid(puzzle, guess, row, col) -> bool:
    """
    Determines whether the guess at the row/col is valid or not
    :param puzzle:
    :param guess:
    :param row:
    :param col:
    :return: bool
    """
    row_val = puzzle[row]
    if guess in row_val:
        return False
    col_val = [puzzle[i][col] for i in range(9)]
    if guess in col_val:
        return False

    # now we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    # now if all the checks pass
    return True


def sudoku_solver(puzzle) -> bool:
    """
    Solve sudoku using backtracking technique
    mutate the puzzle to be the solution if it exists
    :param puzzle:
    :return:bool

    """
    # choose somewhere on the board to make a guess
    row, col = find_next_empty(puzzle)

    # if no more space then we are done
    if row is None:
        return True
    # if there is a space then make a guess between 1 and 9
    for guess in range(1, 10):
        # now we have to check if it is a valid guess
        if is_valid(puzzle, guess, row, col):
            # if the guess is valid then place it in the puzzle
            puzzle[row][col] = guess

            # now we will call the function recursively
            if sudoku_solver(puzzle):
                return True
        # if the guess is not valid or the puzzle is not solved
        # then we will need to backtrack and try a new number
        puzzle[row][col] = -1  # reset the guess to -1

    # if none of the numbers work then the sudoku is unsolvable
    return False


def print_board(puzzle):
    print("Solution of the sudoku puzzle is:")
    for i in range(len(puzzle)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(puzzle[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end="")


def main():
    board = [
        [-1, -1, -1, 2, 6, -1, 7, -1, 1],
        [6, 8, -1, -1, 7, -1, -1, 9, -1],
        [1, 9, -1, -1, -1, 4, 5, -1, -1],
        [8, 2, -1, 1, -1, -1, -1, 4, -1],
        [-1, -1, 4, 6, -1, 2, 9, -1, -1],
        [-1, 5, -1, -1, -1, 3, -1, 2, 8],
        [-1, -1, 9, 3, -1, -1, -1, 7, 4],
        [-1, 4, -1, -1, 5, -1, -1, 3, 6],
        [7, -1, 3, -1, 1, 8, -1, -1, -1],

    ]
    sudoku_solver(board)
    print_board(board)


if __name__ == '__main__':
    main()
