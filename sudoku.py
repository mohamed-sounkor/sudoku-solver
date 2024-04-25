from typing import List
import time
class Variable:
    def __init__(self, row, col, val=0):
        # Initialize attributes
        self.row = row
        self.col = col
        self.value = val
        self.domain = set(range(1, 10))
        self.removed = []

    def remove_from_domain(self, value):
            self.domain.remove(value)
            self.removed.append(value)

    def restore_domain(self):
        self.domain.add(self.removed.pop())

def print_board(bo):
    try:
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")
    
            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
    
                if j == 8:
                    print(bo[i][j].value)
                else:
                    print(str(bo[i][j].value) + " ", end="")
    except:
        print("CAN'T SOLVE !!!")

def initialize_domains(variables: List[Variable]):
    for var in variables:
        if var.value:
            for other_var in variables:
                if other_var != var:
                    if (other_var.row == var.row) or (other_var.col == var.col) or ((other_var.row // 3 == var.row // 3) and (other_var.col // 3 == var.col // 3)):
                        if var.value == other_var.value:
                            return False
    
    for var in variables:
        if var.value:
            var.domain.clear()
            var.domain.add(var.value)
            for other_var in variables:
                if other_var != var:
                    if (other_var.row == var.row) or (other_var.col == var.col) or ((other_var.row // 3 == var.row // 3) and (other_var.col // 3 == var.col // 3)):
                        if not var.domain.isdisjoint(other_var.domain):
                            other_var.domain.difference_update(var.domain)
    return True

def is_consistent(board, variable:Variable, num):
    # Check if the number is not in the same row or column
    for i in range(9):
        if board[variable.row][i].value == num or board[i][variable.col].value == num:
            return False

    # Check if the number is not in the same 3x3 subgrid
    # We need to make it skip checking the same variable we are assigning
    start_row, start_col = 3 * (variable.row // 3), 3 * (variable.col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j].value == num:
                return False

    return True

def forward_check(variables: List[Variable],var:Variable):
    inferenced: List[Variable]= []
    for other_var in variables:
        if other_var != var:
            if (other_var.row == var.row) or (other_var.col == var.col) or ((other_var.row // 3 == var.row // 3) and (other_var.col // 3 == var.col // 3)):
                if var.value in other_var.domain:
                    other_var.remove_from_domain(var.value)
                    inferenced.append(other_var)
                    if len(other_var.domain) == 0:
                        for inferenced_var in inferenced:
                            inferenced_var.restore_domain()
                        var.value = 0
                        return False
    return True

def backTrack_search(puzzle_values: List[int]):
    # Given a 2D list of integers, create a 2D list of 'variable' Objects
    puzzle = [[Variable(row,col) for col in range(9)] for row in range(9)]
    for row in range(9):
        for col in range(9):
            puzzle[row][col] = Variable(row,col,puzzle_values[row][col])
    # Flatten the puzzle list into a single list of variables
    # This List is supposed to be equal to the 'assignment' list in the algorithm pseudo code
    # A list that contains all unassigned variables
    # Once a variable is assigned, it must be removed from the list
    variables = [variable for row in puzzle for variable in row]

    # initialize the domain of every cell based on the given values in the puzzle
    if not initialize_domains(variables):
        return False

    return backTrack(puzzle,variables)

def backTrack(puzzle: List[List[Variable]],variables: List[Variable]):
    # If assginment is complete return assignment
    if 0 not in [i.value for i in variables]:
        return puzzle
    
    # If not, backtrack

    # Applying MRV technique to choose the variable with the least minimum remaining value while ensuring not to choose a variable that has already been set
    # Since the priority is for the 0 index of the tuple, an assigned variable could be chosen twice if their domain is less than the domain of an un-assigned one
    var = min(variables, key=lambda var: (var.value if var.value == 0 else float('inf'), len(var.domain)))

    # Removing the variable from the variables list initially to make sure not to pick it again
    # In case the assignment process failed, the variable must be returned (Not so sure about this point) 
    #variables.remove(var)
    for val in list(var.domain):
        if is_consistent(puzzle,var,val): # If the value is consistent with the already assigned variables
            # Temporarily Assign value to variable
            var.value = val

            # Based on this assignment. Forward check to see if the value will allow future assignments to all neighboring variables
            # and detect inevitable failure based on this assignment if exists
            if forward_check(variables,var):
                
               # Build the rest of the solution based on this value
                if backTrack(puzzle,variables):
                    return puzzle
            #####
                else:    
                    for i in range(9):
                        puzzle[var.row][i].domain.add(var.value)
                        puzzle[i][var.col].domain.add(var.value)

                    start_row, start_col = 3 * (var.row // 3), 3 * (var.col // 3)
                    for i in range(3):
                        for j in range(3):
                            puzzle[start_row + i][start_col + j].domain.add(var.value)
                    var.value=0
            #########
            
    #variables.append(var)
    return False

puzzle_values = [
    [7,0,0,0,0,6,0,0,0],
    [0,0,0,9,0,3,2,6,0],
    [0,0,9,4,0,0,5,0,1],
    [0,0,0,5,0,0,0,1,0],
    [4,7,0,0,0,0,3,0,6],
    [0,1,6,0,0,4,0,0,0],
    [5,9,7,0,1,8,6,4,0],
    [0,6,2,0,4,9,8,3,5],
    [3,0,0,0,2,5,0,0,0],
          ]
start_time = time.perf_counter()
print_board(backTrack_search(puzzle_values))
end_time = time.perf_counter()
print(f'Elapsed time from backend is {end_time - start_time}')
'''solution = backTrack_search(puzzle_values)
if solution:
    print_board(solution)
else:
    print(solution)'''