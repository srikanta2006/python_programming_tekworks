def fact(n):
    if n==0 or n==1:
        return 1
    else:
        fact=1
        i=n
        a1=[]
        while i>=1:
            fact=fact*i
            a1.append(i)
            i-=1
        print(a1)
        return fact
k=int(input("Enter +ve number"))
print(fact(k))