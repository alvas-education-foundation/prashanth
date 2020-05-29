def MissingNo(A): 
    n = len(A) 
    total = (n + 1)*(n + 2)/2
    calsum = sum(A) 
    return total - calsum 
  
# Driver program to test the above function 
l=[]
l=int(input("Enter the array"))
miss = MissingNo(l) 
print(miss)
