def find_empty(grid):
    '''
    This function returns the index (i, j) to the first zero element in a sudoku grid
    If no such element is found, it returns None

    args: grid
    return: A tuple (i,j) where i and j are both integers, or None
    '''

    num_rows = len(grid)
    num_columns = len(grid[0])
    max_empty = max(num_rows, num_columns)
    actual_empty = max_empty

    answer = (num_rows, num_columns, max_empty)

    for r in range(num_rows):
        for c in range(num_columns):
            if grid[r][c] == 0:

                num_empty_col = 0
                for irow in range(num_rows):
                    if grid[irow][c] == 0:
                        num_empty_col += 1
                    if num_empty_col < actual_empty:
                        actual_empty = num_empty_col
                        answer = (r, c)

                num_empty_row = 0
                for icol in range(num_columns):
                    if grid[r][icol] == 0:
                        num_empty_row += 1
                    if num_empty_row < actual_empty:
                        actual_empty = num_empty_row
                        answer = (r, c)

    if actual_empty == max_empty:
        return None

    return answer