def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using a rule-based approach.

    Args:
        board: A 2D list representing the Sudoku board.

    Returns:
        A boolean value indicating whether the puzzle was solved, and the solved board if it was solved.
    """
    # Find an empty cell on the board
    empty_cell = find_empty_cell(board)

    # If there are no empty cells, the board is solved
    if not empty_cell:
        return True, board

    # Try each possible value for the empty cell and recursively solve the board
    row, col = empty_cell
    for value in range(1, 10):
        if is_valid_move(board, row, col, value):
            board[row][col] = value
            solved, solution = solve_sudoku(board)
            if solved:
                return True, solution
            board[row][col] = 0  # Backtrack if the solution was not found

    # If no solution was found, return False
    return False, None


def find_empty_cell(board):
    """
    Finds the first empty cell on the board.

    Args:
        board: A 2D list representing the Sudoku board.

    Returns:
        A tuple representing the row and column of the empty cell, or None if there are no empty cells.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid_move(board, row, col, value):
    """
    Checks if a move is valid for a given cell.

    Args:
        board: A 2D list representing the Sudoku board.
        row: The row index of the cell.
        col: The column index of the cell.
        value: The value to be placed in the cell.

    Returns:
        A boolean value indicating whether the move is valid or not.
    """
    # Check if the value already exists in the row
    if value in board[row]:
        return False

    # Check if the value already exists in the column
    if value in [board[i][col] for i in range(9)]:
        return False

    # Check if the value already exists in the 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    if value in [board[i][j] for i in range(box_row, box_row + 3) for j in range(box_col, box_col + 3)]:
        return False

    # If the value does not violate any rules, it is valid
    return True


def print_board(board):
    """
    Prints the Sudoku board.

    Args:
        board: A 2D list representing the Sudoku board.

    Returns:
        None.
    """
    for row in board:
        print(row)



# Define the Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku puzzle
solved, solution = solve_sudoku(board)

# Print the solution if one was found
if solved:
    print("Solution:")
    print_board(solution)
else:
    print("No solution found.")




