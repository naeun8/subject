import sys

input = sys.stdin.readline

n = int(input())
people = set()

for _ in range(n):
    name, status = input().split()
    if status == "enter":
        people.add(name)
    else:
        people.remove(name)

for name in sorted(people, reverse=True):
    print(name)
