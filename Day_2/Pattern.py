def PatternGen(r,c):
    for i in range(r):
        for j in range(c):
            if ((i+j)==r-1):
                print(" $ ",end='')
            elif (i==j):
                print(" $ ",end='')
                
            else:
                print(" * ",end='')
        print()
r,c=map(int,input("Enter r c").split())   
PatternGen(r,c)
