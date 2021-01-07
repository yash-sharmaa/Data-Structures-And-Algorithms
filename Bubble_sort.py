def bubble_sort(arr, key=None):
    def sortt(arr):
        swapped = 0
        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    swapped = 1

            if not swapped:
                print("Already sorted")
                break
        return print(arr)

    if key:
        subarr = [arr[i][key] for i in range(len(arr))]
        sortt(subarr)

    else:
        sortt(arr)


arr = [
    {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
    {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
]
bubble_sort(arr, 'transaction_amount')
