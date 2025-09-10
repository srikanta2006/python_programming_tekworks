def remove_element(new_list, index):
    new_list=new_list[:index]+new_list[index+1:]
    print(new_list)


new_list=[1,2,3,4,5,6,7,8,9,10]
index=int(input("Enter the index to remove: "))
remove_element(new_list,index)