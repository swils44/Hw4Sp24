#Problem finished by Steven
import numpy as np # import library numpy as alias np
from scipy import linalg
import unicodeit as uni # import library unicodeit as alias uni


def matsolve():
    """
        matsolve function solves a system of linear equations represented by matrices A and B.

        The function prompts the user to input the number of rows and columns for Matrix A and initializes
        two empty NumPy arrays: 'a_arr' for Matrix A and 'b_arr' for Matrix B. The user then inputs the
        elements for each matrix. Matrix A elements are filled row-wise, and Matrix B elements are filled column-wise.

        Parameters:
        None

        Returns:
        None

        Raises:
        ValueError: If the input matrices do not meet the requirements for solving a system of linear equations.


        The function prints both Matrix A and Matrix B to the console and proceeds to check if Matrix A is square
        and if Matrix B has the correct number of rows and only one column. If these conditions are met, the function
        constructs an augmented matrix 'aug_arr' by concatenating Matrix A and Matrix B. Then, it uses the `scipy.linalg.solve`
        function to find the solution 'x' for the system of linear equations.

        Finally, the function prints each solution 'x_i' to the console with subscript formatting using the `unicodit` library.
        If any errors are encountered during the process, appropriate error messages are displayed.

        Note:
        - The function requires NumPy and SciPy libraries to be installed.
        - Ensure that 'unicodit' is available for subscript formatting.

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


    aug_arr = np.concatenate((a_arr, b_arr), axis =1, dtype=float) # Creates the Augmented Matrix aug_arr
    print(f"The augmented matrix of A and B is:")
    print(aug_arr) # print the augmented matrix to the CLI
    x = linalg.solve(a_arr, b_arr) # uses scipy.linalg.solve to solve the matrix's

    for i in range(len(x)):
        # Uses unicodit library to add subscript to x
        print(uni.replace(f"x_{i+1} is {(x[i][0]):.4f}")) # shows the user each of the x value solutions

if __name__ == "__main__":
    matsolve()
