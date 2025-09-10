def BillGen(n):
    bill=0
    if n>300:
        n=n-300
        bill+=7.50*(n)
        n=300
    if n>200:
        n=n-200
        bill+=6.30*n
        n=200
    if n>100:
        n=n-100
        bill+=510*n
        n=100
    if n>50:
        n=n-50
        bill+=4.20*n
        n=50
    if n>0:
        bill+=3.80*n
    return bill
n=int(input("Enter units"))
print(BillGen(n))