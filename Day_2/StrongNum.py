def StrongNum(n):
    i=1
    while i<=n:
        temp=i
        total=0
        while temp>0:
            rem=temp%10
            temp=temp//10
            fact=1
            for j in range(1,rem+1):
                fact=fact*j
            total=fact+total
        if total==i:
            print(f"{i}->Strong number")
        i+=1
n=int(input("Eneter val"))
StrongNum(n)