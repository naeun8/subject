import sys

input = sys.stdin.readline

n = int(input())
books = {}

for _ in range(n):
    title = input().strip()
    books[title] = books.get(title, 0) + 1

max_count = max(books.values())

candidates = [title for title, cnt in books.items() if cnt == max_count]
print(sorted(candidates)[0])
