# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_function( left, right):
    merge_sorted = []
    elements = len(left) + len(right)
    index_left = 0
    index_right = 0

    while len(merge_sorted) < elements: #the loop will run as long as the length of the new array(merge_sorted) is less than the length of original array(len(arr))
        if left[index_left] <= right[index_right]: #if the value on the left is smaller or equal to the value on the right array, add the smaller number to the new array
            merge_sorted.append(left[index_left])
            index_left +=1
        else: 
            merge_sorted.append(right[index_right])
            index_right +=1

        if index_left == len(left): # when the left array is empty end the loop 
            merge_sorted += right[index_right:]
            break

        elif index_right == len(right): # when the right array is empty end the loop 
            merge_sorted += left[index_left:]
            break

    return merge_sorted

def merge_sort(arr):
    middle = len(arr) // 2
    #left = arr[:middle]
    #right = arr[middle:] 

    if len(arr) <=1: 
        return arr
    else:
        #swap values
      left, right = arr[:middle], arr[middle:]

      return merge_function(merge_sort(left), merge_sort(right)) #recursive

    return arr

print(merge_sort([1,94,5,2,8]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
