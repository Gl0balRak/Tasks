def binary(arr, n):
    a, b = 0, len(arr)

    while b-a > 1:
        mid = (a+b)//2
        if arr[mid] == n: return mid
        if n < arr[mid]:
            b = mid
        else:
            a = mid + 1

    return a

arr = [1, 2, 4, 6, 7, 8, 11, 15, 16, 21, 23, 26]

print(arr.insert(binary(arr, 9), 9))
print(arr)
