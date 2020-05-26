def micro(k,l):  
    return k-min(l)


t=int(input('enter number of test case: '))
for j in range(0,t):
    l=[]
    a=int(input('Enter number of elements: '))
    k=int(input('enter the value k : '))
    for i in range(0,a):
        m=int(input())
        l.append(m)
    
    print("time is :",micro(k,l))
