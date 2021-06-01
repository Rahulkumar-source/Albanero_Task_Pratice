def checkOutlier(arr):
    oddCount = 0
    evenCount = 0
    for item in arr:
        if item % 2 == 0:
            evenCount += 1
        else:
            oddCount +=1
            # This is going to print the count of item  if even or odd

#     print(oddCount, evenCount)
    if oddCount == 1:
        for item in arr:
            if item % 2 != 0:
                print(item)
    if evenCount == 1:
        for item in arr:
            if item % 2 == 0:
                print(item)
print(checkOutlier([1,2,3]))
