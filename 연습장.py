import sys
import math

A = sys.stdin.readline().strip('\n')
N = int(A)

def prime(M):
    f = 0
    for i in range(2,M):
        if (M%i)!=0:
            f=1 #소수가 아님
            break
    if f==0:
        print(N)
        return 0
    else:
        return M
    
while True:
    flag=0
    l=math.floor(len(A)/2)
    for i in range(1,l):
        if A[i-1] != A[len(A)-i]:
            flag=1
            N+=1
            break
    if flag==0:
        if prime(N) == 0:
            sys.exit()
        else:
            N+=1
        