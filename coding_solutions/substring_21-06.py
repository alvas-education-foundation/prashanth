def check(string, sub_str): 
    if (string.find(sub_str) == -1): 
        print("NO") 
    else: 
        print("YES") 
            
 
string = input("Enter a string")
sub_str =input("Enter a substring")
check(string, sub_str)
