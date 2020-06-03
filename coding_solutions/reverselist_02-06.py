n = int(input("Enter the size of list : "))
numList = list(int(num) for num in input("Enter the list numbers separated by space: ").strip().split())[:n]
numList.reverse();
print "List : ", numList
