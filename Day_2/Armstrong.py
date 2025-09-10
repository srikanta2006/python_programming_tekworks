def armstrong(n):
    i = 1
    while i <= n:
        temp = i
        total = 0
        while temp > 0:
            digit = temp % 10
            total += digit ** 3   # cube of digit
            temp //= 10
        if total == i:
            print(f"{i} -> is an Armstrong number")
        i += 1

n = int(input("Enter number: "))
armstrong(n)
