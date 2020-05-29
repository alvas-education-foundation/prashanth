N=int(input())
A=list(map(int,input().split()))
maxi=A[N-1]
out=[]
for i in range(N-1,-1,-1):
    if A[i]>=maxi:
        maxi=A[i]
        out.append(maxi)
 
print(*out[::-1])
