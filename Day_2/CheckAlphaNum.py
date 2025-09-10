def CheckAlpha(w):
    if (w.isalpha()):
        if(w>='A' and w<='Z'):
            return "Capital letters"
        else:
            return "Small letters"

    elif (int(w)>=0 and int(w)<=9):
        return "Ti is number"
    else:
        return "Special Character"
i=input("Enter value")
print(CheckAlpha(i))
