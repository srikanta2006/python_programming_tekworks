def occurences(s1, character):
    for i in range(len(s1)):
        if(s1[i]==character):
            print((i+1)," position")

s1=input("Enter string: ")
character=input("Enter the character to check: ")
occurences(s1,character)