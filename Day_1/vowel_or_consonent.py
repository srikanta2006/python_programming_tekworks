def check_vowel(character, vowels):
    if(character.lower() in vowels):
        return "vowel"
    return "consonant"
vowels=['a', 'e', 'i', 'o', 'u']
character=input("Enter the character to check")
print(check_vowel(character, vowels))