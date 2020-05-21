def right_rotate(l,n):
    result=[]
    for i in range(len(l)-n,len(l)):
        result.append(l[i])
    for j in range(0,len(l)-n):
        result.append(l[j]) 
    return result

l=[]
l=int(input("Enter the array to rotate"))
k=int(input('enter number of times to right rotate:'))
print(right_rotate(l,k))
