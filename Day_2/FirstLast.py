def FirstLast(n):
    rem1=n%10
    n=n//10
    while n>1:
        n=n//10
    rem2=n
    a=[]
    a.append(rem1)
    a.append(rem2)
    return a

i =int(input("Enter"))
print(FirstLast(i))