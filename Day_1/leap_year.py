def check_leap_year(year):
    if(year%400==0 or (year%4==0 and year%100!=0)):
        return "Leap year"
    return "Not a leap year"
year=int(input("Enter the year"))
print(check_leap_year(year))
    