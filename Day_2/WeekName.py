def WeekName(w):
    if w==1:
        return "Sunday"
    elif w==2:
        return "Monday"
    elif w==3:
        return "Tuesday"
    elif w==4:
        return "Wednesday"
    elif w==5:
        return "Thursday"
    elif w==6:
        return "Friday"
    elif w==7:
        return "Saturday"
    else:
        return "Enter valid Number"
n=int(input("Enter number "))
print(WeekName(n))