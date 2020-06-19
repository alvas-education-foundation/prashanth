def binaryPallindrome(num): 
     binary = bin(num) 
     binary = binary[2:] 
     return binary == binary[-1::-1] 

num = int(input("enter a number to check whether its binary is palindrome or not"))
print binaryPallindrome(num)
