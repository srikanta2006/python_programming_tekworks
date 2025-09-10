def calculate_duplicates(my_list, unique_list):
    print("Total number of duplicates: ", len(my_list)-len(unique_list))


def unique(my_list):
    unique_list=list(set(my_list))
    return unique_list


my_list=[1,2,2,2,3,4,3,4,5,6,7,8]
unique_list=unique(my_list)
calculate_duplicates(my_list, unique_list)