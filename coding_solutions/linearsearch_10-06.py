def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr =  [int(item) for item in input("Enter thearray of number : ").split()
x = int(inout("Enter the number to be searched"))
print("element found at index "+str(linearsearch(arr,x)))
