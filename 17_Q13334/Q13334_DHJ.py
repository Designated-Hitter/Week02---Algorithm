import sys
N = int(sys.stdin.readline())
home_n_office = []
for _ in range(N):
    x = list((sys.stdin.readline().split()))
    home_n_office.append(x)
d = int(sys.stdin.readline())

possible_commuter = []
for i in home_n_office:
    if abs(int(i[0]) - int(i[1])) < d:
        possible_commuter.append([int(i[0]), abs(int(i[0]) - int(i[1]))])


print(f'N = {N}')
print(f'home_n_office = {home_n_office}')
print(f'possible_commuter = {possible_commuter}')
print(f'd = {d}')
