N, K = map(int, input().split())

max_val = 0

for i in range(1, K+1):
    val = N * i
    reversed_val = int(str(val)[::-1])
    max_val = max(max_val, reversed_val)

print(max_val)
