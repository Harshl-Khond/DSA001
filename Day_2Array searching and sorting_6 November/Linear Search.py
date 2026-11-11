# Linear Search.
def Linear_search(arr, num):
    for i in range(len(arr)):
        if num==arr[i]:
         return f"your array no found at index no {i}"

print(Linear_search([1,2,3,4,5,9,8,7,6],5))        
    