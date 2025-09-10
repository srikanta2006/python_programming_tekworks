def Sumofdigitd(n):
    rem=0
    sum=0
    while n>0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
i=int(input("Enter number"))
print(Sumofdigitd(i))
