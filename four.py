def sorting_algorithm(unsorted_list):
    sorted_list = []
    for x in range(len(unsorted_list)):
        for y in range(len(unsorted_list)-1):       # the last loop is unnecessary hence the -1
            #   In case of equivalent values, do nothing and continue the loop
            if unsorted_list[x] ==  unsorted_list[y]:
                continue
            elif unsorted_list[x] < unsorted_list[y]:
                # if value at position x is less than value at position y, swap values
                temp = unsorted_list[x]
                unsorted_list[x] = unsorted_list[y]
                unsorted_list[y] = temp
    return unsorted_list

print(sorting_algorithm([7,5,3,6,8,9,4,2,1]))















# for y in range(len(unsorted_list)):
        #     if x == unsorted_list[y]:
        #         continue
        #     elif x > unsorted_list[y]:
        #         print('here',unsorted_list[y],'for',x)
        #         temp = unsorted_list[y]
        #         unsorted_list[y] = unsorted_list[y-1]
        #         unsorted_list[y-1] = temp
        #         sorted_list.append(temp)
                # print(unsorted_list[y])
            # elif x < y:
            #     if


