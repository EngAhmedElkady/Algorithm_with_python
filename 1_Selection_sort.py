def selection_sort(lst):
    n=len(lst)              # 5 8 9 0 -2 -5
    for i in range(n-1):
        min_index=i         # min_index=0
        for y in range(i+1,n):
            if lst[y]<lst[min_index]:
                min_index=y
        lst[i],lst[min_index]=lst[min_index],lst[i]

# Time Complexity: O(n2) as there are two nested loops.
# Auxiliary Space: O(1)

if __name__=="__main__":
    # unsorted list
    lst=[5,8,9,0,-2,-5]
    print("before sorted")
    for i in lst :print(i,end=" ")
    print("\nafter sorted ")
    selection_sort(lst)
    for i in lst :print(i,end=" ")


