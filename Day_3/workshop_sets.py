def insert_element(new_list, element):
    new_list.append(element.lower()) 
list_1=[]
n=int(input("Enter the number of applicants on day 1: "))
for _ in range(n):
    ele=input("Enter the mail to register: ")
    insert_element(list_1, ele)

list_2=[]
n=int(input("Enter the number of applicants on day 2: "))
for _ in range(n):
    ele=input("Enter the mail to register: ")
    insert_element(list_2, ele)

list_3=[]
n=int(input("Enter the number of applicants on day 3: "))
for _ in range(n):
    ele=input("Enter the mail to register: ")
    insert_element(list_3, ele)

list_1=set(list_1)
list_2=set(list_2)
list_3=set(list_3)

total_set=(list_1 | list_2 | list_3)
print("Total applicants:", len(total_set))

print("Applicants attended all 3 days:", list_1 & list_2 & list_3)

print("Applicants on single day:",( list_1 ^ list_2) ^ list_3)
