'''
https://www.acmicpc.net/problem/1912
'''

# 제출 답안
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]
for i in range(1,n):
    dp.append(max(dp[-1]+arr[i],arr[i]))
print(max(dp))
