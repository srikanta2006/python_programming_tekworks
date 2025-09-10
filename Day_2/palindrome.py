def checkpalindrome(n):
    i=1
    while i<=n:
        temp=i
        rev=0
        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10
        if rev == i:
            print(f"{i} -> palindrome")
        i += 1

n=int(input("Enter number"))
checkpalindrome(n)
