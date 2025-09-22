def printSolution(board):
    """Print the chessboard configuration."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n") # Prints a newline after each board for separation

def isSafe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe."""
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

# --- Crucial change to solveNQueens for correct counting ---
def solveNQueens(board, row, n):
    """Use backtracking to solve the N-Queens problem and return the count of solutions."""
    if row == n:
        printSolution(board) # Prints the solution
        return 1 # Found one solution, so return 1

    count = 0 # Initialize count for this branch
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1 # Place the queen
            count += solveNQueens(board, row + 1, n) # AGGREGATE solutions from deeper branches
            board[row][col] = 0 # Backtrack

    return count # Return total count for this branch

def nQueens(n):
    """Driver function to solve the N-Queens problem and print total solution count."""
    board = [[0] * n for _ in range(n)]

    # Call solveNQueens and capture the total count it returns
    total_solutions = solveNQueens(board, 0, n)

    if total_solutions == 0:
        print("No solution exists.")
    else:
        print("\n--- All Solutions Printed Above ---")
        print(f"Total number of solutions for {n}-Queens problem: {total_solutions}")

# Solve the 8-Queens problem
nQueens(8)