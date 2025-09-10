def count():
    even=0
    odd=0
    for i in new_list:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    print("Even-", even)
    print("Odd-", odd)


def insert_element(new_list, element):
        new_list.append(element)


new_list=[]
n=int(input("Enter the number of elements: "))
for _ in range(n):
    ele=input("Enter the element to append: ")
    insert_element(new_list, ele)