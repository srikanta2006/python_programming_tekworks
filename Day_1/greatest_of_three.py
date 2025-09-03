def greatest_of_three(a, b, c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c
a,b,c =map(int, input("Enter the three numbers: ").split(" "))
print(greatest_of_three(a,b,c))