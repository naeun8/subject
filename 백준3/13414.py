import sys

input = sys.stdin.readline

k, l = map(int, input().split())

order = {}

for i in range(l):
    student = input().strip()
    order[student] = i  # 마지막 신청만 남김

sorted_students = sorted(order.items(), key=lambda x: x[1])

for student, _ in sorted_students[:k]:
    print(student)
