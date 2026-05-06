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


def multiply(A, B, N):
    result = []

    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        result.append(row)

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] = result[i][j] + A[i][k] * B[k][j]

    return result


def add(A, B, N):
    result = []

    for i in range(N):
        row = []
        for j in range(N):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result



N = int(input("N 입력 (1 < N ≤ 5): "))

A = make_matrix(N)
B = make_matrix(N)
C = make_matrix(N)

print("행렬 A")
print_matrix(A, N)

print("행렬 B")
print_matrix(B, N)

print("행렬 C")
print_matrix(C, N)

AB = multiply(A, B, N)

print("A x B 결과")
print_matrix(AB, N)

result = add(AB, C, N)

print("A x B + C 결과")
print_matrix(result, N)

