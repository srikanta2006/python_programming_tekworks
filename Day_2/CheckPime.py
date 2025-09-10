def checkPrime(n):
    count=0
    i=1
    while(i<=n):
        if n%i==0:
            count+=1
        i+=1
    if(count==2):
        print("Its is a prime NUmber")
    else:
        print("Not a primenumber")

n=int(input("Enter number"))
checkPrime(n)