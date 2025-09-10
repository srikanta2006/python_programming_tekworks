def check_occurences(s):
    freq={}
    for ch in s:
        if(ch in freq):
            freq[ch]+=1
        else:
            freq[ch]=1
    result=""
    for item in freq:
        bit=f"{item}{freq[item]}"
        result=result+bit
    print(result)


s=input("Enter the string: ")
check_occurences(s)