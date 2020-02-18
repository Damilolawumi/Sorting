# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):#-1 is saying once its remaining one item in the unsorted list it should assume thts the highest number
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        for j in range(i+1, len(arr)):
            #if true then set smallst index to iteration index
          if arr[j] < arr[smallest_index]:
            smallest_index = j

        # TO-DO: swap
        if smallest_index != i:
            # Swap the found minimum element with  
            # the first element 
          arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    indexing_length = len(arr) - 1
    sorted = False #we use it to start again anytime the list is being sorted

    while not sorted:
      sorted = True

      for i in range(0, indexing_length):
        if arr[i] > arr[i+1]: #if item to the left is > than item to the right
          sorted = False
           

    return arr

print(bubble_sort([3,4,7,3,6,8,2,1,9,7]))    #added an example

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    return arr