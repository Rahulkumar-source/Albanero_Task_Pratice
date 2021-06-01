def evenOrOdd(arr):
    #arr=[1]
    #evenOrodd(arr)
    if len(arr) == 0 :
        print('even')
    if len(arr) == 1:
        if arr[0] == 0:
            print('even')
        else:
            print('odd')
         
     
    if len(arr) > 1: 
        if sum(arr) % 2 == 0:
            print("even")
        else:
            
            print('odd')

print(evenOrOdd([1])  
