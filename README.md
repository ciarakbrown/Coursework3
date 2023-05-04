coursework3_final contains code with multiple sudoku solvers. it returns full grids, time elapsed and whether the grid is solved correctly.

Requires the following python libaries:
matplotlib.pyplot
numpy


Editing the code:

Open the file coursework3_final.py in IDE of your choice. Python3 is required.
Within the function:
'solve',
uncomment the solver you want to use.
recursive_solve - task 1 
wavefront_solve - task 3. 


Running the code:

Task 1:
After editing, run the file.

Task 2:
ensure that the recursive_solve function is in use to demonstrate the flags. The user needs to define which flag they would like to run. The code includes 4 flags that is set by command line arguments using argparse.

The flags commands are:

- explain True (prints out the answer, provides set of instructions to solve the puzzle. need to add 'True' after flag in terminal)

- file INPUT OUTPUT (Reads grid from a file, solves it and saves it to another file. ("INPUT" refers to which file its reading from, "OUTPUT" refers to the file where the solved grid is going to.)

- hint N (Returns a grid with N values filled in."N" is the amount of values you want filled in. You need to paste the grid that you want the hints for into the give_hint function, and define the grid in the elif statement that calls the hint flag underneath where the main() function is (this is clearly commented in the code to guide the user) then run it from the terminal) 

- profile True (Measures performance, returns the results of how long it takes to solve the grids as a graphical plot. Need to add 'True' after flag in terminal)

Task 3:
After editing, run the file.
