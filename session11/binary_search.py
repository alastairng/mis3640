def binary_search(my_list, x):

    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if x == my_list[mid]:
            return mid
        elif x < my_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
 
 
test_list = [1, 2, 4, , -100, -60000, 123215145, 0, 6223]
test_list.sort()
 

 

    