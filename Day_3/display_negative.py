def insert_element(new_list, element):
    new_list.append(element)

def display_list(new_list):
    for i in new_list:
        if i < 0:
            print(i)

new_list = []
n = int(input("Enter the number of elements: "))
for _ in range(n):
    ele = int(input("Enter the element to append: ")) 
    insert_element(new_list, ele)

display_list(new_list)
