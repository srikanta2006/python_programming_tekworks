p,t,r=map(int, input("Enter P T R ").split(" "))
print("Interest=", p*t*r/100)
print("Total amount in hand=", p+(p*t*r)/100)