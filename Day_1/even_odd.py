def check_even(number):
    if(number%2==0):
        return "Even"
    else:
        return "Odd"
num=int(input("Enter the number: "))
print(check_even(num))