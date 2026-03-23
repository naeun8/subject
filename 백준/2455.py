now = 0
max_people = 0

for _ in range(4):
    out, in_ = map(int, input().split())
    now -= out
    now += in_
    max_people = max(max_people, now)

print(max_people)
