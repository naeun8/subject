import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

count = Counter(cards)

print(*[count[t] for t in targets])
