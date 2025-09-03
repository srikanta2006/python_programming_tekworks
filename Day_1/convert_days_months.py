def convert_days(days):
    years=days//365
    rem_days=days%365
    months=rem_days//30
    rem_days=rem_days%30
    return f'{years} years {months} months {rem_days} days'
total=convert_days(500)
print(total)