import sys
N, K = map(int, sys.stdin.readline().split())

people = []

for i in range(1, N + 1):
    people.append(i)

josephus = []
num = 0 #제거될 사람의 인덱스

for i in range(N):
    num += K-1
    if num >= len(people):
        num = num % len(people)
    josephus.append(str(people.pop(num)))

print('<',", ".join(josephus)[:], '>', sep="")

#메모리: 31256KB
#시간: 40ms