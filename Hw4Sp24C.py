import numpy as np
import unicodeit as uni
import fractions

#Goodbye Steven

def gausselim():
    r = int(input("number of rows: "))
    c = int(input("number of cols: "))
    a_arr = np.empty(shape=(r, c))
    b_arr = np.empty(shape=(r, 1))

    for j in range(r):
        for k in range(c):
            a_arr[j][k] = float(input(f"Enter, A-Matrix element (r,c) {j},{k}: "))

    for i in range(r):
        b_arr[i] = float(input(f"Enter, B-Matrix element (r,c) {i},1: "))

    print(a_arr)
    print(b_arr)

    if a_arr.shape[0] != a_arr.shape[1]:
        print("Error")

    if b_arr.shape[1] > 1 or b_arr.shape[0] != a_arr.shape[0]:
        print("error")
        return

    n = len(b_arr)
    m = n-1
    i = 0
    x = np.zeros(n)
    new_line = "\n"

    aug_arr = np.concatenate((a_arr, b_arr), axis =1, dtype=float)
    print(f"The initial augmented matrix is: {new_line}{aug_arr}")
    print("Solving for the upper triangular matrix:")

    while i < n:

        for p in range(i+1, n):
            if abs(aug_arr[i, i]) < abs(aug_arr[p, i]):
                aug_arr[[p, i]] = aug_arr[[i, p]]

        if aug_arr[i, i] == 0.0:
            print("divide by zero error!")
            return

        for j in range(i+1, n):
            sca_fac = aug_arr[j][i] / aug_arr[i][i]
            sca_fac = np.round(sca_fac, 3)
            print(f"R{j}-({fractions.Fraction(sca_fac).limit_denominator(100)})R{i+1}")

            aug_arr[j] = aug_arr[j] - (sca_fac * aug_arr[i])
            print(np.round(aug_arr))
        i = i + 1

    x[m] = aug_arr[m][n] / aug_arr[m][m]
    for k in range(n - 2, -1, -1):
        x[k] = aug_arr[k][n]

        for j in range(k+1, n):
            x[k] = x[k] - aug_arr[k][j] * x[j]

        x[k] = x[k] / aug_arr[k][k]
    print(f"The following x vector matrix solves the above augmented matrix:")
    for answer in range(n):
        print(uni.replace(f"x_{answer} is {(x[answer])}"))

if __name__ == "__main__":
    gausselim()