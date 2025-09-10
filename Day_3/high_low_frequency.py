def check_occurences(s):
    freq={}
    for ch in s:
        if(ch in freq):
            freq[ch]+=1
        else:
            freq[ch]=1

    min_frequency=min(freq.values())
    max_frequency=max(freq.values())
    
    highest=[ch for ch, count in freq.items() if count==max_frequency]
    lowest=[ch for ch, count in freq.items() if count==min_frequency]
    print(highest, max_frequency)
    print(lowest, min_frequency)


s=input("Enter the string: ")
check_occurences(s)