T = int(input())

VPS_list= []

for i in range(T):
    VPS = input()
    VPS_list.append(VPS)

answer = []

for vps in VPS_list:
    balance = 0 #다루어야 하는 것이 서로 상반되는 2개일 때, 변수에 A라면 +1, B라면 -1 하는 식으로 생각하기 (예: 상승 & 하강, 남성 & 여성 등)

    for i in range(len(vps)):
        if vps[i] == "(":
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            answer = 'NO'
            break

    if balance != 0:
        answer = 'NO'
    else:
        answer = 'YES'

    print(answer)

#메모리: 31256KB
#시간: 48ms