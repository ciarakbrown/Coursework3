grid1 = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]





#First change the grid so it represents the new format, same thing but old grid were values were 0 changes to a list of all possible, eg (1-9)
def convertgrid(grid,n_rows,n_colms):
    new_grid = []

    for x in range(len(grid)):
        new_grid_row = []
        for y in range(len(grid[1])):
            if grid[x][y] == 0:
                new_grid_row.append(list(range(1,n_rows*n_colms)))
            else:
                new_grid_row.append(grid[x][y])
        new_grid.append(new_grid_row)
    return new_grid





#Since some of the grid will be filled out, we can remove the possible values (the ones that represent 0)


#Removes those values from the list but doesnt know which values to remove, need another function to calculate which values need to be removed and what rows they are in. 
def remove_values(grid,rows,colms,number,n_colum,n_rows):
    #removes it from the rows
    for x in range (n_colum * n_rows):
        if isinstance(grid[rows][x], list) and (number) in grid[rows][x]:
            (grid[rows][x]).remove(number)

    #removes it from the columns 
    for y in range(n_colum*n_rows):
        if isinstance(grid[y][colms],list) and number in grid[y][colms] :
            grid[y][colms].remove(number)
    #remove it from square
    d = rows // n_rows
    e = colms //n_colum 
    for a in range(d*n_rows,(d+1)*n_rows):
        for b in range(e*n_colum,(e+1)*n_colum):
            if isinstance(grid[a][b],list)and number in grid[a][b] :
                grid[a][b].remove(number)
    return grid

#Remove all values by inputing all known values into the remove value function
def find_values(grid,n_colms,n_rows):
    for x in range(n_colms*n_rows):
        for y in range(n_colms*n_rows):
            if isinstance(grid[x][y],int):
                grid = remove_values(grid,x,y,grid[x][y],3,3)
            else:
                pass
    return grid


#Function to make the grid neater with printed- copied - only works for 9*9 grid i think- just used for testing
def print_sudoku(sudoku_grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(sudoku_grid[i][j])
            else:
                print(str(sudoku_grid[i][j]) + " ", end="")
        

def find_min_location(grid,n_colm,n_row):
    min_location = (n_colm  *n_row) +1 
    location = []
    
    for x in range (9):
        for y in range(9):
            if isinstance(grid[x][y],list) and len(grid[x][y])< min_location:
                min_location = len(grid[x][y])
                location = [x,y]
                if min_location == 1:
                    print(x+1,y+1)
                    print(grid[x][y])
                    break
    return (location)

    
            



new_list = convertgrid(grid1,3,3)

(print_sudoku(find_values(new_list,3,3)))

