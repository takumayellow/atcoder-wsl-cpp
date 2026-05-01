def count_safe_cells(board):
    # Initialize sets for rows and columns that contain rooks.
    attacked_rows = set()
    attacked_cols = set()
    
    # Scan the board to find rows and columns with rooks
    for i in range(8):
        for j in range(8):
            if board[i][j] == '#':
                attacked_rows.add(i)
                attacked_cols.add(j)
    
    # Total number of cells in the board
    total_cells = 8 * 8
    
    # Cells in rows and columns that are attacked by rooks
    attacked_cells = len(attacked_rows) * 8 + len(attacked_cols) * 8 - len(attacked_rows) * len(attacked_cols)
    
    # Safe cells are those not in attacked rows or columns
    safe_cells = total_cells - attacked_cells
    return safe_cells

# Read input for the board
board = [input().strip() for _ in range(8)]

# Output the count of safe cells
print(count_safe_cells(board))
