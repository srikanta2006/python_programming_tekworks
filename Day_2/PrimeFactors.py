def prime_factors(n):
    print(f"Prime factors of {n}:")
    i = 2
    while i <= n:
        if n % i == 0:
            print(i, end=" ")
            n //= i
        else:
            i += 1

num = int(input("Enter a number: "))
prime_factors(num)
