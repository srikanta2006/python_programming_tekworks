def check_divisibility(num):
    if(num%5==0 and num%11==0):
        return True
    return False
number=int(input("Enter the number: "))
print(check_divisibility(number))