def merge(a, b):
    c = []
    i = j = 0
    while(i < len(a) and j < len(b)):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        c = c + b[j:]
    else:
        c = c + a[i:]
    return c


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left, right = merge_sort(arr[:len(arr) // 2]), merge_sort(arr[(len(arr) // 2):])

    return merge(left, right)


print(merge_sort([3, 4, 72, 36, 43, 84, 93, 21, 74]))
