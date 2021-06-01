def retrunEvenOnly(arr):
    oddArr = []
    evenArr = []
    for item in arr:
        if item % 2 == 0:
            evenArr.append(item)
        if item % 2 == 1:
            oddArr.append(item)
    return evenArr
print(retrunEvenOnly([1, 2, 3, 4, 5, 6, 7, 8]))
