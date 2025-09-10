def counter(str):
    alpha=0
    num=0
    spl=0
    for item in str:
        if(item.isalpha()):
            alpha=alpha+1
        elif(item.isdigit()):
            num=num+1
        else:
            spl=spl+1
    print("aplhabets:", alpha)
    print("numbers:", num)
    print("special characters:", spl)


s1=input("Enter string: ")
counter(s1)