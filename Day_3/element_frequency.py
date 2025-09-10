from collections import Counter
def print_frequency(my_list):
    freq=Counter(my_list)
    for i in freq:
        print(i, "->", freq[i])



my_list=[1,2,2,2,3,4,3,4,5,6,7,8]
print_frequency(my_list)