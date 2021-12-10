# 제출 답안
import sys
N = int(sys.stdin.readline())
target = list(int(sys.stdin.readline()) for _ in range(N))
s = []
ans = ''
for i in range(1,N+1):
    s.append(i)
    ans += "+"
    while(s):
        if s[-1] == target[0]:
            s.pop()
            ans += "-"
            del target[0]
        else:
              break
print("NO") if s else print(*ans,sep='\n')



'''
# 문제 정의
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.
'''
