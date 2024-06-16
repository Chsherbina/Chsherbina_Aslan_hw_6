def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, x):
    first = 0
    last = len(arr) - 1
    unknown = False
    pos = -1

    while first <= last and not unknown:
        middle = (first + last) // 2
        if arr[middle] == x:
            unknown = True
            pos = middle
        else:
            if x < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1

    if unknown:
        print("Элемент найден на позиции:", pos)
    else:
        print("Элемент не найден")


numbers = [17, 55, 38, 19, 105, 33, 69]
sorted_list = bubble_sort(numbers)
print("Отсортированный список:", sorted_list)

element_to_search = 19
binary_search(sorted_list, element_to_search)