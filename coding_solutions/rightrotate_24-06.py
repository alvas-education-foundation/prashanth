l1 = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
n=int(input("Enter no of times to rotate))
l1 = l1[-n:] + l1[:-n] 
print(l1)
