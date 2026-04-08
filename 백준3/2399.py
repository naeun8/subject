import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

prefix = 0
result = 0

for i in range(n):
    result += arr[i] * i - prefix
    prefix += arr[i]

print(result * 2)
