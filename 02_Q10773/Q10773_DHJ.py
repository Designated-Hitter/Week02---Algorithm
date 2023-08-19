import sys
K = int(sys.stdin.readline())
integers = []
for i in range(K):
    integers.append(int(sys.stdin.readline()))

answer = []
for integer in integers:
    if integer == 0:
        answer.pop()
    else:
        answer.append(int)

print(sum(answer))

#메모리: 32820 KB
#시간: 84 ms