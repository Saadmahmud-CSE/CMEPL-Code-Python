N = int(input("Please Enter the size of the equation system n: "))

def gaussianElimination(mat):
    singular_flag = forwardElim(mat)
    if (singular_flag != -1):
        print("Singular Matrix.")
        if (mat[singular_flag][N]):
            print("Inconsistent System.")
        else:
            print("May have infinitely many solutions.")
        return
    backSub(mat)

def swap_row(mat, i, j):
    for k in range(N + 1):
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp

def forwardElim(mat):
    for k in range(N):
        i_max = k
        v_max = mat[i_max][k]
        for i in range(k + 1, N):
            if (abs(mat[i][k]) > v_max):
                v_max = mat[i][k]
                i_max = i
        if not mat[k][i_max]:
            return k
        if (i_max != k):
            swap_row(mat, k, i_max)
        for i in range(k + 1, N):
            f = mat[i][k] / mat[k][k]
            for j in range(k + 1, N + 1):
                mat[i][j] -= mat[k][j] * f
            mat[i][k] = 0
    return -1

def backSub(mat):
    x = [None for _ in range(N)]
    for i in range(N - 1, -1, -1):
        x[i] = mat[i][N]
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]
        x[i] = (x[i] / mat[i][i])
    print("\nAns = ")
    for i in range(N):
        print("\t{:.4f}".format(x[i]))

mat = [[1, 2, 3, 3], [2, 3, 4, 1], [2, 5, 6, 2]]
gaussianElimination(mat)