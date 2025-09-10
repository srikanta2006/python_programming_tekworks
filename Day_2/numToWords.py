def numtowords(n):
    rem=0
    count=0
    a=[]
    while n>0:
        rem=n%10
        n=n//10
        count+=1
        if rem==1:
            a.append("one")
        if rem==2:
            a.append("two")
        if rem==3:
            a.append("three")
        if rem==4:
            a.append("four")
        if rem==5:
            a.append("five")
        if rem==6:
            a.append("six")
        if rem==7:
            a.append("seven")
        if rem==8:
            a.append("eight")
        if rem==9:
            a.append("nine")
        if rem==0:
            a.append("zero")
    for i in range(len(a)-1,-1,-1):
        print(a[i])
i =int(input("Enter"))
numtowords(i)
        
        
