def compare(s1, s2):
    if(s1==s2):
        print("Both the strings are same")
    elif(s1>s2):
        print(s1+" is greater than "+s2)
    else:
        print(s2+" is greater than "+s1)

s1=input("Enter first string: ")
s2=input("Enter the second string: ")
compare(s1, s2)