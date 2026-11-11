def Rotate_array_K(arr, k):
    arr1=[]
    arr2=[]
    for i in range(len(arr)):
        if i<=k:
            arr1.append(arr[i])
        else :
            arr2.append(arr[i])
    return arr2 + arr1     

print(Rotate_array_K([1,2,3,4,5,6,7,8,9,10],3))           