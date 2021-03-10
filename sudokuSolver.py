import numpy as np

# Load sudokus
sudoku = np.load("data/hard_puzzle.npy")
print("very_easy_puzzle.npy has been loaded into the variable sudoku")
print(f"sudoku.shape: {sudoku.shape}, sudoku[0].shape: {sudoku[0].shape}, sudoku.dtype: {sudoku.dtype}")

# Load solutions for demonstration
solutions = np.load("data/hard_solution.npy")

def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """    
    # setup variables for solovver
    # domain array stores the number of possible domains for all variables (9x9 array)
    domainArray = getDomainArray(sudoku)
    # nextVariable stores the row and column indexes of the next variable (1x2 array)
    nextVariable = pickNextVariable(domainArray)
    # variableValues stores a set of possible values that the speific variable can have
    variableValues = getVariableDomain(sudoku, nextVariable[0], nextVariable[1])
    # copies the sudoku
    newSudokuState = sudoku
    # get the original value from the sudoku before it is changed & updated
    originalValue = sudoku[nextVariable[0], nextVariable[1]]
    # setup empty array to return if no solutions are found
    empty = np.full((9, 9), -1, dtype=int)
    # loop through each of the possible values for the variable
    for value in variableValues:
        # set the variable to the value
        newSudokuState[nextVariable[0], nextVariable[1]] = value
        # if the sudoku is now solved return it otherwise...
        if isGoalState(newSudokuState):
            return newSudokuState
        # check if the sudoku is valid
        if checkSudokuValid(newSudokuState):
            # if valid, perform depth first search of the states trying to find the solution
            deepState = sudoku_solver(newSudokuState)  
            # check whether the deepstate returned is not empty and if it is the goal state
            if not((deepState==empty).all()) and isGoalState(deepState):
                # if not empty, and is goal state then return
                return deepState
        # if sudoku isn't valid then revert the variable's value and try with next value
        newSudokuState[nextVariable[0], nextVariable[1]] = originalValue
    # if all values for the variable have been exhausted then return the empty array
    return empty
    

def isValid(array):
    # remove 0's from array
    array = np.delete(array, np.argwhere(array == 0))
    # if the length of array is the same as the length of the unique values in array then return true
    # otherwise return false as there must be duplicate values
    return len(np.unique(array)) == len(array)
    
def checkRowValid(sudoku, rowIndex):
    # get the row from the sudoku
    row = sudoku[rowIndex]
    return isValid(row)
    
def checkColumnValid(sudoku, columnIndex):
    # get the column from the sudoku
    column = sudoku[:, columnIndex]    
    return isValid(column)

def checkSquaresValid(square):
    return isValid(square)

def getSquares(sudoku):
    # create empty 9x9 array to place squares into
    # loop through the sudoku
    squares = []
    finalSquares = np.empty((9, 9), dtype=int) 
    counter = 0
    # adapted from https://bit.ly/3v5U8Jk
    # loop through the sudoku, grabbing 3 variables at a time to create a 3x3 square
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            squares = []
            squares.append(sudoku[i][j:j+3])
            squares.append(sudoku[i+1][j:j+3])
            squares.append(sudoku[i+2][j:j+3])
            # turn the squares array into a 1D array with all values for the square in one index
            finalSquares[counter] = np.array(squares).flatten()
            counter += 1
    return finalSquares

# returns whether the sudoku is valid or not
def checkSudokuValid(sudoku):
    # get the squares
    squares = getSquares(sudoku)
    # loop through checking each column, row and square
    for i in range(9):
        if checkColumnValid(sudoku, i) == False:
            return False
        elif checkRowValid(sudoku, i) == False:
            return False
        elif checkSquaresValid(squares[i]) == False:
            return False
    # if none of the rows, columns or squares are invalid then the sudoku must be valid so return true
    return True

# function to find the index of a square based on the row and column indexes
def findSquareIndex(row, column):
    temp = row // 3
    box = temp * 3
    temp = column // 3
    box += temp
    return box

# returns a set of remaining domain values the given array has remaining
def getDomain(variableArray):
    variableArray = set(variableArray)
    possibleDomain = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return possibleDomain - variableArray

# return a set of the possible domain values a variable has
def getVariableDomain(sudoku, row, column):
    # get row's domain
    rowDomain = getDomain(sudoku[row])
    # get column's domain
    columnDomain = getDomain(sudoku[:,column])
    # calculate all squares
    squares = getSquares(sudoku)
    # calculate the index of the square
    squareIndex = findSquareIndex(row, column)
    # get square's domain
    squareDomain = getDomain(squares[squareIndex])
    # intersection of all domains to give the possible list of domains for the variable
    variableDomains = rowDomain & columnDomain & squareDomain
    return variableDomains

# returns an array of the number domains each variable has available
def getDomainArray(sudoku):
    # initialise 9x9 array filled with 10
    domainArray = np.full((9, 9), 10, dtype=int)
    for i in range(9):
        for j in range(9):
            # if the sudoku square is 0 then set the domain array index to the number of domains of that variable
            if sudoku[i][j] == 0:
                domainArray[i][j] = len(getVariableDomain(sudoku, i, j))
    return domainArray

# returns whether sudoku is in goal state or not
def isGoalState(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True

# returns an array that contains row & column indexes for next variable to update
# taken from https://stackoverflow.com/a/30180322
def pickNextVariable(domainArray):
    return divmod(domainArray.argmin(), domainArray.shape[1])


