def BinarySearch(a,key):
    low  = 0
    high = len(a)-1
    while low<=high:
        mid = (low + high) // 2
        if a[mid] == key:
            return  True
        elif a[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return  False
list1 = [1,3,5,7,9]
found = BinarySearch(list1,9)
print(found)
