def check_neg(num):
    if(num<0):
        return "Negitive"
    return "Positive"
num=int(input("Enter the number: "))
print(check_neg(num))