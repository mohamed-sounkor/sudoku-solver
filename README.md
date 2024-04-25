# sudoku-solver
Sudoku solver using backtracking with GUI. 

# Sudoku Solver using Backtracking and Constraint Satisfaction

This program is a Sudoku solver that utilizes the backtracking algorithm enhanced with the MRV (Minimum Remaining Value) heuristic, forward checking, and constraint propagation techniques. The Sudoku problem is formalized as a Constraint Satisfaction Problem (CSP).

## Problem Description

Sudoku is a logic-based number puzzle that consists of a 9x9 grid divided into nine 3x3 subgrids. The objective is to fill the grid with digits from 1 to 9, such that each row, each column, and each subgrid contains all the digits from 1 to 9 without repetition.

## Constraint Satisfaction Problem (CSP) Formulation

In this program, the Sudoku problem is formulated as a CSP, where:

- Variables: Each cell of the Sudoku grid is represented as a variable. There are a total of 81 variables in a 9x9 Sudoku grid.

- Domain: The domain of each variable represents the possible values that can be assigned to that cell. The domain of each variable is initially set to {1, 2, 3, 4, 5, 6, 7, 8, 9}.

- Constraints: The constraints in the Sudoku problem are as follows:
  1. All values in a row must be distinct.
  2. All values in a column must be distinct.
  3. All values in a 3x3 subgrid must be distinct.

## Solver Algorithm

The solver algorithm utilizes the backtracking algorithm with the following enhancements:

1. Minimum Remaining Value (MRV) Heuristic: The MRV heuristic is used to select the variable with the least number of remaining values in its domain. This helps in selecting the most constrained variable first, improving the efficiency of the algorithm.

2. Forward Checking: After assigning a value to a variable, forward checking is performed to propagate constraints and update the domains of the neighboring variables. If a variable's domain becomes empty, it indicates an inevitable failure, and the algorithm backtracks.

3. Constraint Propagation: While assigning a value to a variable, constraint propagation is performed to update the domains of the neighboring variables based on the assigned value. This helps in reducing the search space by eliminating values that are no longer valid.

## Usage

To use the Sudoku solver program, follow these steps:

1. Ensure you have Python installed on your system.

2. Open the command line or terminal.

3. Execute the following command to run the solver:

   ```
   python sudoku_GUI_v5.0.py
   ```

4. The program will load with empty sudoku board, enter your puzzle values and the program will solve the Sudoku puzzle and display the solved grid on the GUI.

## Input Format

There are 2 ways to interact with this program, either from the sudoku_solver.py file or from the GUI file.
in the sudoku_solver.py file: 
- The Sudoku puzzle is represented as a 9x9 grid in the `puzzle_values` list in the code. The empty cells are represented by 0, and the filled cells contain the respective values from 1 to 9.
- You can modify the `puzzle_values` list in the code to input your own Sudoku puzzle.

in the GUI file, you just run the file and feed your puzzle values to the cells in the GUI

## Output Format
in case of sudoku_solver.py file, the solved sudoku problem will be displayed in the terminal.
in case of GUI file, The solved Sudoku grid will be displayed on the GUI in a 9x9 grid format. The solved values will be indicated with disabled entries.

## Performance

The solver utilizes various techniques to improve performance. However, the performance may vary depending on the complexity of the Sudoku puzzle. Solving easier puzzles usually takes less time, while harder puzzles may take more time.

The code is provided with functions that measures precisely the time elapsed in solving each puzzle wich is displayed in the terminal.

## Features

The program have the following features:
- GUI to enter the puzzle values and display the results.
- 'New puzzle' button to clear the board.
- 'Solve' button to solve the current puzzle.
- Level setting menu to set the difficulty level of a new puzzle.
- 'Generate puzzle' button to display a preloaded puzzle with difficulty level that corresponds to the level set from the above menu.

The program was developed by [Your Name] as an exercise or project.

## License

This program can be used and modified freely for personal and educational purposes.
