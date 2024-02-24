#Problem finished by Steven
import numpy as np # import library numpy as alias np
import unicodeit as uni # import library unicodeit as alias uni
import fractions # import library fractions

def gausselim():
    """

    :return:
    """
    # Create variables r and c ro represent rows and columns
    r = int(input("number of rows: "))
    c = int(input("number of cols: "))
    # Creates two empty arrays. The first is Matrix A of size [r x c] and Matrix B is of size [r x 1]
    a_arr = np.empty(shape=(r, c))
    b_arr = np.empty(shape=(r, 1))

    # Iterates over the created row and column variables and has the user input each of the elements in both the
    # A and B Matrix
    for j in range(r):
        for k in range(c):
            a_arr[j][k] = float(input(f"Enter, A-Matrix element (r,c) {j},{k}: ")) # Has the user input the elements of
            # Matrix A

    for i in range(r):
        # Has the user input the elements of the B Matrix
        b_arr[i] = float(input(f"Enter, B-Matrix element (r,c) {i},1: "))

    print(a_arr) # Prints the A Matrix to the CLI
    print(b_arr) # Prints the B Matrix to the CLI

    # Checks to see if the A Matrix is Square
    if a_arr.shape[0] != a_arr.shape[1]:
        print("Error")
    # Checks to see if the B matrix has the same number of rows as the A Matrix and checks if B only has one column
    if b_arr.shape[1] > 1 or b_arr.shape[0] != a_arr.shape[0]:
        print("error")
        return

    n = len(b_arr) # Gets the length of Matrix B
    m = n-1 # Subtracts 1 from the length of Matrix B
    i = 0 # Initialize a variable I for looping
    x = np.zeros(n) # Creates an empty array of size n
    new_line = "\n" # Creates a newline character to use in formatting later

    aug_arr = np.concatenate((a_arr, b_arr), axis =1, dtype=float) # Creates the Augmented Matrix aug_arr
    print(f"The initial augmented matrix is: {new_line}{aug_arr}") # prints the new Augmented Matrix to the CLI
    print("Solving for the upper triangular matrix:") # Informs the user that the program is about to solve for the
    # upper triangular Matrix by using row manipulation and back-solving

    # Gaussian Elimination with Partial Pivoting for solving a system of linear equations

    # Iterate over rows
    while i < n:

        # Partial Pivoting: Find the maximum element in the current column and swap rows
        for p in range(i + 1, n):
            if abs(aug_arr[i, i]) < abs(aug_arr[p, i]):
                aug_arr[[p, i]] = aug_arr[[i, p]]

        # Check if the pivot element is zero, which would cause division by zero
        if aug_arr[i, i] == 0.0:
            print("divide by zero error!")
            return

        # Eliminate lower triangular elements below the pivot
        for j in range(i + 1, n):
            sca_fac = aug_arr[j][i] / aug_arr[i][i]
            sca_fac = np.round(sca_fac, 3)

            # Display the elimination operation
            print(f"R{j + 1} - ({fractions.Fraction(sca_fac).limit_denominator(100)})R{i + 1}")

            aug_arr[j] = aug_arr[j] - (sca_fac * aug_arr[i])

            # Display the updated augmented matrix after elimination
            print(np.round(aug_arr))

        i = i + 1

    # Back-substitution to find the solution vector x
    x[m] = aug_arr[m][n] / aug_arr[m][m]

    for k in range(n - 2, -1, -1):
        # Back-substitution: Solve for each variable in reverse order
        x[k] = aug_arr[k][n]

        # Subtract known values to find the unknown variable
        for j in range(k + 1, n):
            x[k] = x[k] - aug_arr[k][j] * x[j]

        # Normalize by the coefficient of the variable
        x[k] = x[k] / aug_arr[k][k]

    # Display the solution vector
    print(f"The following x vector matrix solves the above augmented matrix:")

    for answer in range(n):
        # Uses unicodit library to add subscript to x
        print(uni.replace(f"x_{answer} is {(x[answer])}")) # shows the user each of the x value solutions

if __name__ == "__main__":
    gausselim()