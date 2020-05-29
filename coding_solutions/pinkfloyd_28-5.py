l=list()
c=0
n=int(input())
for i in range(0,n):
 l=int(input())
for i in range(0,len(l)-1):
    if l[i]<=l[i+1]:
        c=1
    else:
        c=0
        break
if c==0:
    print('Pink is Happy')
else:
    print('Pink is Sad')

