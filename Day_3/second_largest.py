def second_largest():
    n_list=sorted(new_list)
    print(n_list[-2])



def insert_element(new_list, element):
    new_list.append(element)


new_list=[]
n=int(input("Enter the number of elements: "))
for _ in range(n):
    ele=input("Enter the element to append: ")
    insert_element(new_list, ele)

second_largest()