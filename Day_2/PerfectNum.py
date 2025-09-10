def perfectNum(n):
    i=1
    while i<=n:
        a=[]
        for j in range(1,i):
            if i%j==0:
                a.append(j)
        if sum(a)==i:
            print(f"{i}->is perfect number")
        i+=1
n=int(input("Enter"))
perfectNum(n)