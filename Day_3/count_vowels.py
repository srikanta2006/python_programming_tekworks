vowels=['a', 'e', 'i', 'o', 'u']
def count_vowels(str):
    vowel=0
    consonant=0
    for item in str:
        if((item.lower()) in vowels):
            vowel=vowel+1
        else:
            consonant=consonant+1
    print("vowles", vowel)
    print("consonants", consonant)
str=input("Enter the string: ")
count_vowels(str)