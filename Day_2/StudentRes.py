def GradeGEn(m):
    if m>=40:
        if m<50:
            return 'c'
        elif m>50 and m<71:
            return 'b'
        elif m>70 and m<81:
            return 'a'
        else:
            return "distinction"
    else:
        return 'f'
i=int(input("Enter"))
print(GradeGEn(i))