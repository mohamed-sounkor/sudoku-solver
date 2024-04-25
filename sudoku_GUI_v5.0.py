import tkinter as tk
from tkinter import messagebox
from sudoku import backTrack_search
import time
import copy

ez = [
      [0,2,0,1,7,0,5,0,3],
      [0,5,0,0,0,0,0,2,7],
      [0,0,0,6,5,0,0,9,0],
      [2,1,0,4,0,7,0,3,0],
      [7,3,4,8,0,0,0,0,1],
      [0,0,5,0,3,1,0,0,0],
      [0,0,8,7,0,4,0,1,9],
      [3,0,2,0,0,0,7,8,0],
      [1,9,0,0,8,6,0,5,0]
      ]
medium = [
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
hard = [
        [0,8,0,3,0,0,0,0,2],
        [6,1,0,0,0,0,5,4,9],
        [0,5,7,4,0,0,8,0,1],
        [0,0,0,0,0,0,0,0,6],
        [0,3,2,0,0,0,0,0,7],
        [1,0,0,0,7,0,2,0,0],
        [0,7,8,6,0,0,4,1,0],
        [0,0,9,0,1,0,0,6,0],
        [5,0,0,0,0,0,0,0,8]
        ]
expert = [
    [6,0,0,0,0,0,8,0,0],
    [0,0,0,0,9,0,0,4,5],
    [0,5,7,2,0,4,0,0,0],
    [0,6,9,0,1,0,0,0,0],
    [5,0,1,7,0,0,0,0,0],
    [0,0,0,0,2,8,0,6,1],
    [0,0,0,0,0,2,0,0,4],
    [9,0,0,0,3,0,0,5,0],
    [7,0,8,5,0,9,6,0,3]
    ]
master = [
        [0,8,3,7,0,1,6,0,0],
        [0,4,0,0,0,0,0,0,5],
        [0,0,0,0,8,0,0,0,0],
        [0,0,0,0,9,0,2,0,0],
        [0,3,0,2,0,8,0,4,0],
        [0,0,8,0,6,0,0,0,0],
        [0,0,0,9,0,0,0,0,0],
        [0,0,1,3,0,2,7,0,0],
        [7,0,0,0,0,0,0,6,0]
        ]
extreme = [
    [8,7,0,0,0,0,0,9,0],
    [0,0,0,0,0,8,0,0,1],
    [0,0,0,0,2,0,0,5,0],
    [0,0,0,4,3,2,0,0,0],
    [0,1,9,5,0,0,0,0,0],
    [0,6,0,1,0,0,0,0,0],
    [1,0,0,0,0,0,4,0,3],
    [0,0,4,0,0,5,2,0,0],
    [0,0,3,0,0,0,0,0,0]
    ]


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.board_values = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = []  # Store a reference to the entries
        self.example = [
            [0,0,2,4,0,9,7,0,0],
            [5,0,0,0,0,0,0,0,2],
            [6,7,0,2,0,8,0,1,4],
            [8,0,4,0,7,0,1,0,3],
            [0,0,1,8,0,3,2,0,0],
            [3,0,6,0,9,0,4,0,8],
            [9,1,0,5,0,4,0,3,6],
            [4,0,0,0,0,0,0,0,1],
            [0,0,3,9,0,1,5,0,0]]
        self.create_gui()
    def on_button_click(self,difficulty_var):
            selected_difficulty = difficulty_var.get()
            #return selected_difficulty
            print(selected_difficulty)
            self.sample_puzzle(selected_difficulty)
    def create_gui(self):
        # Create the canvas for the Sudoku board
        cell_size = 60
        canvas = tk.Canvas(self.root, width=9 * cell_size, height=9 * cell_size)
        canvas.pack()

        # Create entries for each cell in the Sudoku grid
        for i in range(9):
            row_entries = []
            for j in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18))
                x = j * cell_size + cell_size // 2
                y = i * cell_size + cell_size // 2
                canvas.create_window(x, y, window=entry, anchor=tk.CENTER)
                row_entries.append(entry)
            self.entries.append(row_entries)

        for i in range(0, 10):
            width = 2 if i % 3 == 0 else 1
            color = "black" if i % 3 == 0 else "gray"
            
            canvas.create_line(i * cell_size, 0, i * cell_size, 9 * cell_size, width=width, fill=color)
            canvas.create_line(0, i * cell_size, 9 * cell_size, i * cell_size, width=width, fill=color)

        solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle)
        solve_button.pack()

        new_puzzle_button = tk.Button(self.root, text="New Puzzle", command=self.clear_board)
        new_puzzle_button.pack()
        # Create a list of difficulty levels
        difficulties = ["Easy", "Medium", "Hard", "Expert", "Master", "Extreme"]
        
        # Create a variable to store the selected difficulty
        difficulty_var = tk.StringVar(self.root)
        difficulty_var.set(difficulties[0])  # Set the default difficulty
        
        # Create a dropdown menu (combobox) for difficulty selection
        difficulty_menu = tk.OptionMenu(self.root, difficulty_var, *difficulties)
        difficulty_menu.pack()
        
        # Create a button to trigger the sample_puzzle function
        generate_button = tk.Button(self.root, text="Generate Puzzle", command=lambda: self.on_button_click(difficulty_var))
        generate_button.pack()
        
        x= '''easy_button = tk.Button(self.root, text="Easy", command=lambda : self.sample_puzzle(1))
        easy_button.pack()
        medium_button = tk.Button(self.root, text="Medium  ", command=lambda : self.sample_puzzle(2))
        medium_button.pack()
        hard_button = tk.Button(self.root, text="Hard  ", command=lambda : self.sample_puzzle(3))
        hard_button.pack()
        expert_button = tk.Button(self.root, text="Expert  ", command=lambda : self.sample_puzzle(4))
        expert_button.pack()
        master_button = tk.Button(self.root, text="Master  ", command=lambda : self.sample_puzzle(5))
        master_button.pack()
        extreme_button = tk.Button(self.root, text="Extreme  ", command=lambda : self.sample_puzzle(6))
        extreme_button.pack()'''

    
    def update_values(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(state='normal')
                value = self.entries[i][j].get()
                self.board_values[i][j] = int(value) if value.isdigit() and 1 <= int(value) <= 9 else 0
    def display_values(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, 'end')
                if str(self.board_values[i][j]).isdigit():
                    if int(self.board_values[i][j]) ==0:
                        self.entries[i][j].insert(0,'')
                    else:
                        self.entries[i][j].insert(0, str(self.board_values[i][j]))
                        self.entries[i][j].config(state=tk.DISABLED)

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(state='normal')
                self.entries[i][j].delete(0, 'end')
                self.board_values[i][j] = 0

    def solve_puzzle(self):
        self.update_values()
        start_time = time.perf_counter()
        solution = backTrack_search(self.board_values)
        end_time = time.perf_counter()
        print(f'Elapsed time is from GUI is {end_time - start_time}')
        if solution:
            for row in range(9):
                for col in range(9):
                    self.board_values[row][col] = solution[row][col].value
            self.display_values()
        else:
            messagebox.showerror("Information", "Can't solve the puzzle. Please check the input.")
        #print(temp)
        #print_board(self.board_values)
    def copy_example(self,temp):
        self.clear_board()
        if temp == "Easy":
            for row in range(9):
                for col in range(9):
                    self.board_values[row][col] = ez[row][col]
        if temp == "Medium":
            for row in range(9):
                for col in range(9):
                    self.board_values[row][col] = medium[row][col]
        elif temp == "Hard":
            for row in range(9):
                for col in range(9):
                    self.board_values[row][col] = hard[row][col]
        elif temp == "Expert":
            for row in range(9):
                for col in range(9):
                    self.board_values[row][col] = expert[row][col]
        elif temp == "Master":
            for row in range(9):
                for col in range(9):
                    self.board_values[row][col] = master[row][col]
        elif temp == "Extreme":
            for row in range(9):
                for col in range(9):
                    self.board_values[row][col] = extreme[row][col]
                    
    def sample_puzzle(self,temp):
        self.copy_example(temp)
        #self.board_values = copy.copy(puzzle_values)
        #print(self.board_values)
        self.display_values()
    
def main():
    root = tk.Tk()
    sudoku_gui = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
