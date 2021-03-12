# SudokuSolver
My Approach
For my algorithm I decided upon using the recommended constraint satisfaction algorithm with a depth-first search. This algorithm works efficiently and solves every test sudoku (bar one) within 30 seconds when tested on linux.bath.ac.uk. 

The depth-first search algorithm I used was based upon the eight queen’s problem algorithm that was shown in the lecture material however a few changes were made to ensure it worked correctly. The algorithm firsts creates a 9x9 array which stores the number of domains for each variable in the sudoku. This means the algorithm can find which of the variables has the smallest number of domains to check since this means less branching is required. Once it had this array and found the variable with the minimum remaining domain values, it found the actual domain values for this variable. The algorithm then created a new sudoku board and looped through each of the domain values for the variable. On each loop it checked whether the sudoku board was in the goal state (i.e. the board had no 0's in it), and whether the board is valid (does not contain any repetitions on any columns, rows or 3x3 squares). If the board was valid but not in the goal state, then the algorithm recursively called itself with the new sudoku board. This recursive call carried on until the sudoku board was completed, or an invalid sudoku state was found. When an invalid state occurred, the sudoku board would return to the previous board's formation and try a different variable value. This continued until every domain value had been checked for the variable. If no valid states could be found, then the board would again revert to the previous formation and this process repeats. If no valid formation can be found for the sudoku then the algorithm returns a 9x9 array filled with -1, signalling that the sudoku is unsolvable.
One change that had to be made to the original eight queens problem’s algorithm was ensuring the variable was reverted back to the original value after each of the domain values had been tried. This ensured that the board did not store the variable values from previous depth-searches. Another change that I made was instead of returning 'None' in the algorithm if no solutions were found, it instead returned a 9x9 array filled with -1 which shows that no solution is possible.

My Decisions
One problem that I encountered was choosing whether I wanted to implement a 9x9x10 3D array that stored a list of all possible domain values for each variable, or instead create a 9x9 2D array that stored the number of domain values for each variable, and then calculate the domain values for each variable when needed. In the end I chose the second option as I believed manipulating and using a 3D array would be difficult and the array indexing would be difficult. Although the first option may be more efficient, when testing my implementation I found that almost all sudoku's were solved within the time limit, and eleven of the fifteen hard sudokus were solved in under 10 seconds. Solving these sudokus in this good time made me happy in my chosen solution.
In order to check each row, column and 3x3 square was valid I created an algorithm that took in an array of 9 integers and returned whether there were any duplicate numbers in the array. This works very well, however as the 3x3 squares are not a 1D dimension array this required me to change the square array into a 1D array. This was done using the flattern() function. This allowed me to reuse the same function isValid() to check whether each row, column and square was valid.
Another problem I encountered was how I would update the domainArray after each variable had a new value assigned to it. One solution would be to rerun the getDomainArray() function which returns the domain array again. However, this requires to iterate over every variable in the sudoku. This is slow and unneeded as only the domains of each variable in the row, columnn and square that the variable is located in actualy have to be updated, rather than every variable in the sudoku. In the end I choose the first solution to this problem and recalculated the domain array as each variable is updated. This is because the required logic to subtract only one from each of the row, column & square domain array values would be very difficult to implement so I did not end up doing it in this way. 

References
Anil Kemisetti. 2021. Solving Sudoku … Think Constraint Satisfaction Problem | by Anil Kemisetti | My Udacity Ai Nanodegree Notes | Medium. [ONLINE] Available at: https://medium.com/my-udacity-ai-nanodegree-notes/solving-sudoku-think-constraint-satisfaction-problem-75763f0742c9. [Accessed 12 March 2021].
Reddit. 2021. How to divide 9X9 matrix into nine 3X3 matrices?. [ONLINE] Available at: https://www.reddit.com/r/learnpython/comments/dpnm0x/how_to_divide_9x9_matrix_into_nine_3x3_matrices/f5x1q8l?utm_source=share&utm_medium=web2x&context=3. [Accessed 12 March 2021].
Stack Overflow. 2021. python - Numpy: get the column and row index of the minimum value of a 2D array - Stack Overflow. [ONLINE] Available at: https://stackoverflow.com/a/30180322. [Accessed 12 March 2021].
Constraint Satisfaction With Sudoku • steven.codes. 2021. Constraint Satisfaction With Sudoku • steven.codes. [ONLINE] Available at: https://steven.codes/blog/constraint-satisfaction-with-sudoku/. [Accessed 12 March 2021].
Moodle: CM20252 Artificial Intelligence. 2021. Week 2: Informed Search and Constraint Satisfaction. [ONLINE] Available at: https://moodle.bath.ac.uk/mod/resource/view.php?id=974662. [Accessed 12 March 2021].