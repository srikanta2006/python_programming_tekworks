def insert_element(new_list, element):
    new_list.append(element)
    print(new_list)


new_list=[]
n=int(input("Enter the number of elements: "))
for _ in range(n):
    ele=input("Enter the element to append: ")
    insert_element(new_list, ele)
