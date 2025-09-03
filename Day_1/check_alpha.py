def check_alpha(character):
    if(character.isalpha()):
        return "Alphabet"
    return "Not alphabet"
data=input("enter character: ")
print(check_alpha(data))