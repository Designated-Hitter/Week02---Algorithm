#Kruskal 알고리즘
# 간선들을 정렬해야 하므로 간선 개수가 적을 때
import sys
V, E = map(int, sys.stdin.readline().split())

V_root = [i for i in range(V + 1)] #root를 저장하는 V_root배열 (여기서 root는 연결요소 중 가장 작은 값)
E_list = [] #간선들의 리스트

for _ in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    E_list.append([start, end, weight])

E_list.sort(key=lambda x:x[2]) #리스트 안의 요소들(리스트)을 요소내 2번째 인덱스(가중치) 기준으로 정렬

def find(x):
    if x != V_root[x]:
        V_root[x] = find(V_root[x])
    return V_root[x]

answer = 0
for s, e, w in E_list:
    s_root = find(s)
    e_root = find(e)
    if s_root != e_root:
        if s_root > e_root:
            V_root[s_root] = e_root
        else:
            V_root[e_root] = s_root
        answer += w

print(answer)

#Prim 알고리즘

