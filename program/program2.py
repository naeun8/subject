import random

def make_matrix(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            num = random.randint(1, N*N*10 - 1)
            row.append(num)
        matrix.append(row)
    return matrix


def print_matrix(matrix, N):
    for i in range(N):
        for j in range(N):
            print("%4d" % matrix[i][j], end=" ")
        print()
    print()


def transpose(A, N):
    result = []

    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        result.append(row)

    for i in range(N):
        for j in range(N):
            result[j][i] = A[i][j]

    return result



N = int(input("N 입력 (1 < N ≤ 5): "))

A = make_matrix(N)

print("원본 행렬 A")
print_matrix(A, N)

T = transpose(A, N)

print("전치 행렬")
print_matrix(T, N)

