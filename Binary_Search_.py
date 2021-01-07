k = [6, 28, 31, 37, 41, 49, 58]


def binary_search(arr, target):
    l = 0
    r = len(arr) - 1

    mid = (l + r) // 2
    counter = 0
    while(l <= r):
        counter += 1
        if arr[mid] == target:
            return mid, counter
        if arr[mid] < target:
            l = mid + 1
            mid = (l + r) // 2
        if arr[mid] > target:
            r = mid - 1
            mid = (l + r) // 2

    return "Target not in List"


print(binary_search(k, 31))
