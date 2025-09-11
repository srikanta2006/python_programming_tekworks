n1=int(input("Enter the divident: "))
n2=int(input("Enter the divisor: "))
try:
    result=n1/n2
    print(result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!!")

finally:
    print("Execution completed!")