# SudokuSolver

A Sudoku puzzle consists of 81 cells which are divided into nine columns, rows and regions. The task is now to place the numbers from 1 to 9 into the empty cells in such a way that in every row, column and 3×3 region each number appears only once ([sudoku-space.com](http://www.sudoku-space.com/sudoku.php)). 

E.g. The left-hand Sudoku shows what is initially given, with the right-side showing the solved Sudoku.


![Example soduoku](https://github.com/fj317/SudokuSolver/blob/master/images/sudoku.png)

I decided to implement a depth-first search algorithm using constraint satisfaction to efficiently solve Sodokus. The algorithm used stores the number of domains for each variable in the Sudoku. This means the algorithms starts with the variable with the smallest number of domains and helps to reduce the number of branches required. The algorithm then performs a depth-first search on this variable, recursively calling itself until either the Sudoku is in the goal state (i.e. it was solved and correct), or the Sudoku is found to be unsolveable.

The algorithm works well and was able to solve every Soduku given to it within 30 seconds.

There are 4 different Sodukus that can be given as input, starting from 'very_easy' to the most difficult 'hard' Sudokus. Change the input load lines to reflect the Sudokus that you wish to use as input. 
