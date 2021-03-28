# Bubble Sort is the simplest sorting algorithm that works by repeatedly
# swapping the adjacent elements if they are in wrong order.
# i want make the large number in the end
def Bubble_sort(lst):    #o(n^2)
    n=len(lst)
    for i in range(n-1):           # the index start from 0 to len-1   

        for y in range(n-1-i): # len-1-i because i will move the large number to the end every loop

            if lst[y]>lst[y+1]:

                lst[y],lst[y+1]=lst[y+1],lst[y];



if __name__=="__main__":
    lst=[5 ,1, 4, 2, 8]   # unsorted list
    Bubble_sort(lst)
    for i in lst:  print(i,end=" ")


# Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

# Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

# Auxiliary Space: O(1)


# First Pass:
# ( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
# ( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
# ( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

# Second Pass:
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
# ( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
# Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

# Third Pass:
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

