import sys
sys.setrecursionlimit(10**9)

def post (start, end):
    if start > end:
        return
    mid = end + 1 #오른쪽에 노드가 없는 경우
    for i in range(start + 1, end + 1): #for 문을 통해 num_list[start], 다시말해 루트보다 커지면 오른쪽 노드
        if num_list[i] > num_list[start]:
            mid = i #왼쪽 트리와 오른쪽 트리가 나뉘는 부분
            break
    post(start + 1, mid - 1) #왼쪽 트리
    post(mid, end) #오른쪽 트리

    print(num_list[start]) #루트 출력
       


num_list = []
#입력량이 정해지지 않은 상황에서 입력값 받기
#에러가 발생한다면 try-catch문에서 except가 발생하게 되고 여기에 break를 넣어둔다
while True:
    try: 
        num = int(sys.stdin.readline())
        num_list.append(num)
    except:
        break

post(0, len(num_list) - 1)  
#전위순회를 했으므로 루트보다 큰 원소가 나오는 지점이 왼쪽 서브 트리와 오른쪽 서브 트리가 나뉘는 지점

#50 - root
#30 24 5 28 45 - 왼쪽
#98 52 60 - 오른쪽