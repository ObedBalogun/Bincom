#   Implementing Binary Search


#   bubble sort works on the assumption that the array has been sorted
################################################## My Approach ##################################################

def binary_search(array,target):
    mid = len(array)//2
    if target == array[mid]:
        print('Target is a position {0}'.format(mid))
    elif target > array[mid]:
        for x in array[mid:]:
            if x == target:
                print('Found in second half of array at position',array.index(x))
    elif target < array[mid]:
        for y in array[:mid]:
            if target == y:
                print('Found in first half of array at position',array.index(y))
    else:
        print('element not in array')


binary_search([2,3,4,5,6],7)
################################################## End of My Approach ##################################################



def binarySearch(array,lower,target,upper=None):
    # upper can be understood as upper = len(array)-1
    # if the length of the array isn't known
    if upper == None:
        upper = len(array)-1

    if upper >= lower:
        mid = (lower+upper) // 2
        if target == array[mid]:
            return "Element found in the array at position {0}".format(array.index(target))
        elif target < array[mid]:
            return binarySearch(array,lower,target,mid-1)
        else:
            return binarySearch(array,mid+1,target,upper)
    else:
        return 'Element not found in array'


print(binarySearch([1,2,3,4,5,6,7],0,3))

#  My assumption is that the beginning of every array is 0
