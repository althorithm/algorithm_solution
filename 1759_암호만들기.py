
def backtracking(password,j_cnt,m_cnt): # 암호 후보, 자음 개수, 모음 개수
    
    if len(password) == N and j_cnt >= 2 and m_cnt >= 1: # 조건을 충족하면 암호리스트에 반환
        answer.append(password)

    for i in arr:
        
        if i in password: continue #중복 패스
        if ord(i) < ord(password[-1]): continue # 증가하눈 순서 배열이 아니면 패스

        if dic[i] == 1: # 모음이리면 
            backtracking(password + i, j_cnt , m_cnt + 1)
        else: # 자음이라면 
            backtracking(password + i , j_cnt + 1 , m_cnt)

import sys
from collections import defaultdict

input = sys.stdin.readline

N , M = map(int,input().split())
arr = input().rstrip().split()
dic = defaultdict(int)
answer = []

for i in ['a','e','i','o','u']:
    dic[i] = 1

for j in arr:
    if dic[j] == 1:
        backtracking(j,0,1)
    else:
        backtracking(j,1,0)

answer = sorted(answer)

for ans in answer:
    print(ans)

