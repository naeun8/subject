N = int(input())

for i in range(2 * N):
    if i % 2 == 0:
        print("* " * ((N + 1) // 2))
    else:
        print(" *" * (N // 2))
