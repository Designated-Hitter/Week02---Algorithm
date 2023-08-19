import sys
N = int(sys.stdin.readline())
bars = []
for i in range(N):
    bars.append(int(sys.stdin.readline()))

right_bar = bars[-1]
highest_bar = right_bar
count = 1
bars.pop()

for i in range(N - 1):
    if bars[-1] <= highest_bar:
        bars.pop()
    elif bars[-1] > highest_bar:
        count += 1
        highest_bar = bars[-1]
        bars.pop()

print(count)

#메모리: 35108 KB
#시간: 104ms