import sys

input = sys.stdin.readline

n, m = map(int, input().split())

hear = {input().strip() for _ in range(n)}
see = {input().strip() for _ in range(m)}

result = sorted(hear & see)

print(len(result))
print(*result, sep="\n")
