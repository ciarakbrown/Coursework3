"""
Adding a header to the file.
"""
import random
import copy
import time
import argparse

from matplotlib import pyplot as plt
import math
import numpy as np
import csv
#Grids 1-4 are 2x2
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
    [0, 6, 0, 9, 0, 0, 1, 0, 8]]  # easy1

grid8 = [
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 1],
    [3, 6, 9, 0, 8, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 6, 8, 0, 0],
    [0, 0, 0, 1, 3, 0, 0, 0, 9],
    [4, 0, 5, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 6, 0, 0, 7, 0, 0, 0],
    [1, 0, 0, 3, 4, 0, 0, 0, 0]]  # med1

grid9 = [[0, 2, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 6, 0, 4, 0, 0, 0, 0],
    [5, 8, 0, 0, 9, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 3, 0, 0, 4],
    [4, 1, 0, 0, 8, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 5],
    [2, 0, 0, 0, 1, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 0, 0, 8, 0, 5, 7]]  # hard1

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3), (grid7, 3, 3), (grid8, 3, 3), (grid9, 3, 3)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''
parser = argparse.ArgumentParser()

parser.add_argument("-explain",help= "Explain solving",type=bool)
parser.add_argument("-file", help= "Path to the file input",nargs=2, type = str)
parser.add_argument("-hint", help= "Return a hint", nargs=1, type = int)
parser.add_argument("-profile", help = "Measures performance of your solver, in terms of time", type =bool  )

args=parser.parse_args()

print("arg explain is ", args.explain)
print("path", args.file)
print("hint", args.hint)
print("profile is", args.profile)


def give_hint(grid, n_rows, n_cols):
    solution = recursive_solve(grid, n_rows, n_cols)
    hint_grid = [row[:] for row in grid]
    hint_count = 0

    for r in range(n_rows * n_cols):
        for c in range(n_rows * n_cols):
            if hint_count == args.hint:
                break
            if grid[r][c] == 0:
                hint_grid[r][c] = solution[r][c]
                hint_count += 1
            return hint_grid
        else:
            continue

# def open_file(input_file):
#     with open(input_file, 'r') as f:
#         lines = f.readlines()
#         grid = []
#         for line in lines:
#             nums = []
#             for char in line.strip():
#                 if char.isdigit():
#                     nums.append(int(char))
#             grid.append(nums)
#         print(grid)
    
#     return grid

# def output_file(output_file, solved_grid):
#     with open(output_file, 'w') as f:
#         for row in solved_grid:
#             f.write(','.join(str(num) for num in row))
#             f.write('\n')
    
    
def file_input(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        grid = [[int(number) for number in row] for row in reader]
    return grid

def file_output(filename, sudoku_board):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in sudoku_board:
            writer.writerow(row)


# def explain(grid):
#         # final_grid = ''
#         # for i in range (len(grid)):
#         #     final_grid += (grid[i])

#         exp_string = ''
#         for x in range (0,len(grid)):
#             for y in range (0,len(grid[x])):
#                 if grid[x][y] != 0:
#                     exp_string +=(f'Put {grid[x][y]} in location ({x}, {y})\n')

#         return_list = (exp_string)
#         return return_list



def time_diff_grids(solver, grid, sub_rows, sub_cols):
    """
    function that runs a sudoku solver 5 times
    and returns the average time elapsed to solve
    """

    times = []

    #  run each solver 5 times
    for _ in range(5):
        start_time = time.time()
        solver_result = solver(grid, sub_rows, sub_cols)
        elapsed_time = time.time() - start_time

        #  if solver cannot solve grid, set time taken to a 'maximum' (50)
        if check_solution(solver_result, sub_rows, sub_cols) is False:
            elapsed_time = 31

        #  add these 5 times to a list
        times.append(elapsed_time)

    #  sum the list and divide by 5 to find average
    average_time = sum(times)/5
    return average_time

from task3 import wavefront_solve

def profile(grid_list):
    average_times_random = []
    average_times_recursive = []
    average_times_wavefront = []

    #  loop through each grid
    for grid, sub_rows, sub_cols in grid_list:
        newgrid = copy.deepcopy(grid)  # make copy of original

        #  run the timer
        # append to list containing average time to solve each grid
        answers = time_diff_grids(random_solve, newgrid, sub_rows, sub_cols)
        average_times_random.append(answers)

        #  same for recursive
        newgrid = copy.deepcopy(grid)
        answers = time_diff_grids(recursive_solve, newgrid, sub_rows, sub_cols)
        average_times_recursive.append(answers)

        #  same for wavefront
        newgrid = copy.deepcopy(grid)
        answers = time_diff_grids(wavefront_solve, newgrid, sub_rows, sub_cols)
        average_times_wavefront.append(answers)

    random_times_grid1 = average_times_random[0]
    random_times_grid2 = average_times_random[1]
    random_times_grid3 = average_times_random[2]

    recursive_times_grid1 = average_times_recursive[0]
    recursive_times_grid2 = average_times_recursive[1]
    recursive_times_grid3 = average_times_recursive[2]

    wavefront_times_grid1 = average_times_wavefront[0]
    wavefront_times_grid2 = average_times_wavefront[1]
    wavefront_times_grid3 = average_times_wavefront[2]

    solver_type = ("Random", "Recursive", "Wavefront")
    difficulty = {
        'Easy Grid': (random_times_grid1, recursive_times_grid1, wavefront_times_grid1),
        'Medium Grid': (random_times_grid2, recursive_times_grid2, wavefront_times_grid2),
        'Hard Grid': (random_times_grid3, recursive_times_grid3, wavefront_times_grid3),
    }

    x = np.arange(len(solver_type))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in difficulty.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Time (s)')
    ax.set_title('Method of solving')
    ax.set_xticks(x + width, solver_type)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 0.013)

    plt.show()

    print('if time = 0, solver is unsuccessful')


# def main_args(*args):
#     #if args.explain:
#         #print(explain(grid1,2,2)[0] ,'\n' + explain(grid1,2,2)[1])
#     if args.hint:
#         args.hint = int(args.hint)
#         give_hint(grid, n_rows, n_cols)
#     if args.profile:
#         profile()
#     #if args.explain and args.hint:
#         #explain(give_hint(grid, n_rows, n_cols))

def main_args(*args):
    
    if args.file != None:
        grid = file_input(args.file[0])
        n_rows = math.ceil(math.sqrt(len(grid)))
        n_cols = math.floor(math.sqrt(len(grid[0])))
        solved_grid = recursive_solve(grid,n_rows, n_cols)
    
        file_output(args.file[1],solved_grid)

    if args.hint!= None :
        args.hint[0] = int(args.hint)
        give_hint(grid, n_rows, n_cols)
        print(give_hint(grid, n_rows, n_cols))

def check_section(section, n):
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
        return True
    return False


def get_squares(grid, n_rows, n_cols):
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

    return squares


def check_solution(grid, n_rows, n_cols):
    '''
    This function is used to check whether a sudoku board has been correctly solved
    args: grid - representation of a suduko board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''

    if grid is None:
        return False

    n = n_rows * n_cols

    for row in grid:
        if not check_section(row, n):
            return False

    for i in range(n_rows * n_cols):
        column = []
        for row in grid:
            column.append(row[i])

        if not check_section(column, n):
            return False

    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if not check_section(square, n):
            return False

    return True


def get_subgrids(grid, sub_grid_rows, sub_grid_cols):
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


def find_empty(grid, sub_grid_rows, sub_grid_cols):
    """
    This function returns the index (i, j, k) to the first zero element in a sudoku grid
    If no such element is found, it returns None
    args: grids - a list of tuples, where each tuple contains a sudoku grid and the number of rows and columns in each sub-grid
    return: A tuple (i,j,k) where i, j, and k are all integers, or None
    """

    num_rows = len(grid)
    num_cols = len(grid[0])
    full_set = set()

    for i in range(1, num_rows+1):
        full_set.add(i)

    found_empty = False
    best_bag = full_set.copy()
    answer = None

    subgrid_coordinates = get_subgrids(grid, sub_grid_rows, sub_grid_cols)

    #  iterate through grid looking for empties
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                found_empty = True
                bag = full_set.copy()

                #  search rows
                for irow in range(num_rows):
                    if grid[irow][c] != 0:
                        bag.discard(grid[irow][c])

                #  search cols
                for icol in range(num_cols):
                    if grid[r][icol] != 0:
                        bag.discard(grid[r][icol])

                #  determine which subgrid that empty cell is in
                for subgrid in subgrid_coordinates:
                    if (r, c) in subgrid:
                        empty_subgrid = subgrid  # this is the subgrid that contains the empty cell

                for j, k in empty_subgrid:
                    sub_grid_value = grid[j][k]
                    if sub_grid_value != 0:
                        bag.discard(sub_grid_value)

                if len(bag) < len(best_bag):
                    best_bag = bag
                    answer = r, c, best_bag

    if not found_empty:
        return None

    return answer


def recursive_solve(grid, n_rows, n_cols):
    """
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found
    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    """

    empty = find_empty(grid, n_rows, n_cols)

    if not empty:
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            return None

    else:
        row, col, bag = empty
        for i in bag:
            grid[row][col] = i
            ans = recursive_solve(grid, n_rows, n_cols)
            if ans:
                return ans
            grid[row][col] = 0

    return None


def random_solve(grid, n_rows, n_cols, max_tries=50000):
    """
    This function uses random trial and error to solve a Sudoku grid

    args: grid, n_rows, n_cols, max_tries
    return: A solved grid (as a nested list), or the original grid if no solution is found
    """

    for i in range(max_tries):
        possible_solution = fill_board_randomly(grid, n_rows, n_cols)
        if check_solution(possible_solution, n_rows, n_cols):
            return possible_solution

    return grid


def fill_board_randomly(grid, n_rows, n_cols):
    """
    This function will fill an unsolved Sudoku grid with random numbers

    args: grid, n_rows, n_cols
    return: A grid with all empty values filled in
    """
    n = n_rows*n_cols
    #  make a copy of the original grid
    filled_grid = copy.deepcopy(grid)

    #  Loop through the rows
    for i in range(len(grid)):
        #  Loop through the columns
        for j in range(len(grid[0])):
            #  If we find a zero, fill it in with a random integer
            if grid[i][j] == 0:
                filled_grid[i][j] = random.randint(1, n)

    return filled_grid 

def solve(grid, n_rows, n_cols):

    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''
    
    #return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)



"""
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
"""

def main():

    points = 0

    print("Running test script for coursework 1")
    print("====================================")
    
    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i+1))
        start_time = time.time()
        solution = solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        print(solution)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i+1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i+1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
    main()
