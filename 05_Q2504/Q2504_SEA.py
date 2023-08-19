s = input()

ans = 0
temp = 1
stack = []
"""
우선 a * (b + c) = a * b + a * c 이다
그리고 올바른 괄호열이 아닌 경우를 예외처리 해주었기 때문에
무조건 올바른 괄호열이 올것이다라고 가정한 후,
(가 나오면 temp에 *2, [가 나오면 temp에 *3을 해주고 이후 )가 나오면 temp를 ans에 더해주고 //2을 하고 ]가 나오면 더햊고 temp //3를 해주면 된다. 
닫히는 괄호가 여는 괄호 바로 이후에 나올 때는 ()[]가 완성된거라 스택 팝 해준다.
여기서 스택의 역할: 괄호문자열이 올바른 괄호열인가
"""
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        temp *= 2
    elif s[i] == '[':
        stack.append(s[i])
        temp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] == '[': # 비어있거나 맨 마지막 값이 (가 아니면 잘못된 입력
            ans = 0
            break

        # 그 외의 경우에 s[i-1]값이 (면 ()라는 소리다.
        if s[i - 1] == '(':
            ans += temp
        
        # '(' 아니면 )]라는거고 이는 이미 ans에 추가된 값이라서 무시한다.
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break

        if s[i - 1] == '[':
            ans += temp
        
        stack.pop()
        temp //= 3

# 나왔을 때 스택에 아직 남아있으면 부적절한 입력값
if stack:
    print(0)
else:
    print(ans)
            
