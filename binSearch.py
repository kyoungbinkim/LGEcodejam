
def binarySearch(l, val):
    low, high = 0, len(l)-1
    while low <= high:
        mid = (low+high)//2

        if l[mid] == val:
            return mid
        elif l[mid] > val:
            high = mid -1
        else:
            low = mid + 1
    return -1
