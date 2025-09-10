def SumFirstLast(n):
    rem1=n%10
    n=n//10
    if n==0:
        return rem1
    if n>=1 and n<=9:
        return (rem1+n)
    while n>1:
        n=n//10
    rem2=n
    a=[]
    a.append(rem1)
    a.append(rem2)
    return sum(a)
i=int(input("Enter num"))
print(SumFirstLast(i))