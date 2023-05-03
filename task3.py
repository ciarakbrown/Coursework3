import copy
import time
import argparse
import matplotlib.pyplot as plt
import random


grid1 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 3, 4],
    [3, 4, 2, 1]]

grid2 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 0, 4],
    [3, 4, 2, 1]]

grid3 = [
    [1, 0, 4, 2],
    [4, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid4 = [
    [1, 0, 4, 2],
    [0, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid5 = [
    [1, 0, 0, 2],
    [0, 0, 1, 0],
    [0, 1, 0, 4],
    [0, 0, 0, 1]]

grid6 = [
    [0, 0, 6, 0, 0, 3],
    [5, 0, 0, 0, 0, 0],
    [0, 1, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 1, 0, 0, 0],
    [0, 5, 0, 0, 6, 4]]

grid7 = [
    [9, 0, 6, 0, 0, 1, 0, 4, 0],
    [7, 0, 1, 2, 9, 0, 0, 6, 0],
    [4, 0, 2, 8, 0, 6, 3, 0, 0],
    [0, 0, 0, 0, 2, 0, 9, 8, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 9, 4, 0, 8, 0, 0, 0, 0],
    [0, 0, 3, 7, 0, 8, 4, 0, 9],
    [0, 4, 0, 0, 1, 3, 7, 0, 6],
    [0, 6, 0, 9, 0, 0, 1, 0, 8]]  

grid8 = [
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 1],
    [3, 6, 9, 0, 8, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 6, 8, 0, 0],
    [0, 0, 0, 1, 3, 0, 0, 0, 9],
    [4, 0, 5, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 6, 0, 0, 7, 0, 0, 0],
    [1, 0, 0, 3, 4, 0, 0, 0, 0]]  

grid9 = [
    [0, 2, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 6, 0, 4, 0, 0, 0, 0],
    [5, 8, 0, 0, 9, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 3, 0, 0, 4],
    [4, 1, 0, 0, 8, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 5],
    [2, 0, 0, 0, 1, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 0, 0, 8, 0, 5, 7]]  

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3), (grid7, 3, 3), (grid8, 3, 3), (grid9, 3, 3)]


def check_section(section, n):
    """ Checks that the section is correct by checking the length and size of the numbers within the grid
        args: section -
        returns: True(the section is correct), False(the section is not correct)
    """

    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n + 1)]):
        return True
    return False


def get_squares(grid, n_rows, n_cols):
    """ Gets each subgrid of the suduko and adds then into a list, where each element in the list is a list with the elements from one square
        args: grid- Representation of a suduko board as a nested list. , n_rows- The number of rows in the squares of the grid, n_cols- The number of columns in the squares of the grid
        Returns: List containing the squares, where each square is represented as a list within the list
"""





    squares = []
    for i in range(n_cols):
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            cols = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            squares.append(square)

    return (squares)



def check_solution(grid, n_rows, n_cols):
    '''
    This function is used to check whether a sudoku board has been correctly solved

    args: grid - representation of a suduko board as a nested list.
    Returns: True (correct solution) or False (incorrect solution)
    '''
    n = n_rows * n_cols

    for row in grid:
        if check_section(row, n) == False:
            return False

    for i in range(n_rows * n_cols):  
        column = []
        for row in grid:
            column.append(row[i])

        if check_section(column, n) == False:
            return False

    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if check_section(square, n) == False:
            return False

    return True






def get_subgrids(grid, sub_grid_rows, sub_grid_cols):
    """It takes in the grid representing the sudoku, and returns a list representing the coordinates of each cell within the subgrid 
    
    args:sub_grid_rows-The number of rows in each subgrid ,sub_grid_cols- the number of columns in subgrid
    Returns:subgrids- returns a list of subgrids where each list is representing the coordinates of the cells within the subgrid 
    
    
    
    """
    
    subgrids = []
    num_rows = len(grid)
    num_cols = len(grid[0])

    for r in range(0, num_rows, sub_grid_rows):
        for c in range(0, num_cols, sub_grid_cols):
            subgrid = []
            for ir in range(r, r + sub_grid_rows):
                for ic in range(c, c + sub_grid_cols):
                    subgrid.append((ir, ic))

            subgrids.append(subgrid)
    return subgrids

def find_empty_wavefront(grid, sub_grids, available_data):
    """ 
    Finds the first empty cell and returns its coordinate, finds the sub_grid index and available value 
    Args: sub_grid- a list of subgrids, representing the coordinates of each cell in the sub_grid, 
    available_data- contains available values for sub-grid,row and column
    
    Returns: ans- contains row index, column index, subgrid index and available values of the first empty cell,
    or None (when there is no empty cell)
    """
    
    ans = None
    best_intersection = set()
    for i in range(1 + len(grid)):
        best_intersection.add(i)

    sub_grid_available, row_available, col_available = available_data
    sub_grids_len = len(sub_grids)
    for sub_grid_index in range(sub_grids_len):
        sub_grid = sub_grids[sub_grid_index]
        for coord in sub_grid:
            r, c = coord
            if grid[r][c] == 0:
                intersection = sub_grid_available[sub_grid_index] & row_available[r] & col_available[c]

                if len(intersection) == 1:
                    return (r, c, sub_grid_index, intersection)  
                elif len(intersection) < len(best_intersection):
                    best_intersection = intersection
                    ans = (r, c, sub_grid_index, best_intersection)
    return ans


def recursive_wavefront(grid, n_rows, n_cols, sub_grids, available_data):
    next_cell = find_empty_wavefront(grid, sub_grids, available_data)
    """ Checks to see if solved, is incorrect or removes possible values. When removing possible values,
    if it ends up being the correct value we return it, if its not, it restores the grid and try a different value.
    args: sub_grids-, available_data- 
    Returns: None(If there is no solution), or the solved grid 
        
    """

    if not next_cell:

        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
 
            return None
    else:
        row, col, sub_grid_index, bag = next_cell


        for i in bag:

            
            sub_grid_available, row_available, col_available = available_data
            sub_grid_available[sub_grid_index].discard(i)
            row_available[row].discard(i)
            col_available[col].discard(i)
            new_available_data = (sub_grid_available, row_available, col_available)
            grid[row][col] = i
          
            ans = recursive_wavefront(grid, n_rows, n_cols, sub_grids, new_available_data)
 
            if ans:
                return ans


            sub_grid_available[sub_grid_index].add(i)
            row_available[row].add(i)
            col_available[col].add(i)
            available_data = (sub_grid_available, row_available, col_available)

            grid[row][col] = 0

            
    return None


def initial_available(grid, n_rows, n_cols, sub_grids):
    """ Returns the available values for each empty cell in the grid 
        args: List of the coordinate of each cell within the subgrid 
        returns: 3 lists of the available values for each empty cell 
        in the row subgrid and column
    """
    
    
    sub_grid_available = []
    row_available = []
    col_available = []

    num_rows = len(grid)
    num_columns = len(grid[0])

    all_poss = set()
    for poss in range(1, 1 + (n_rows * n_cols)):
        all_poss.add(poss)


    for sub_grid in sub_grids:
        sub_grid_poss = all_poss.copy()
        for coord in sub_grid:
            r, c = coord
            if grid[r][c] != 0:
                sub_grid_poss.discard(grid[r][c])
        sub_grid_available.append(sub_grid_poss)

    
    for row in range(num_rows):
        row_poss = all_poss.copy()
        for col in range(num_columns):
            if grid[row][col] != 0:
                row_poss.discard(grid[row][col])
        row_available.append(row_poss)

    
    for col in range(num_columns):
        col_poss = all_poss.copy()
        for row in range(num_rows):
            if grid[row][col] != 0:
                col_poss.discard(grid[row][col])
        col_available.append(col_poss)

    return (sub_grid_available, row_available, col_available)


def wavefront_solve(grid, n_rows, n_cols):
    """Calls  the functions and returns the solved grid
        return: The solved grid 
    """
    
    sub_grids = get_subgrids(grid, n_rows, n_cols)
    available_data = initial_available(grid, n_rows, n_cols, sub_grids)
    return recursive_wavefront(grid, n_rows, n_cols, sub_grids, available_data)

def main():
    """
    Returns the grid, the time taken to solve the grid, and if the grid is correct or not 
    """
    
    
    points = 0

    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))
        start_time = time.time()
        solution = wavefront_solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        print(solution)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i + 1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i + 1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
    main()
