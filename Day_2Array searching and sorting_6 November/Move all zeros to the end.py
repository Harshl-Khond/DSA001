# Move all zeros to the end.
def Remove_all_zeroes(arr):
    array_of_zeroes=[]
    array_of_non_zeroes=[]
    for i in arr:
        if arr[i]==0:
            array_of_zeroes.append(arr[i])
        else:
            array_of_non_zeroes.append(arr[i])
    return array_of_non_zeroes + array_of_zeroes   

print(Remove_all_zeroes([1,2,3,0,4,0,5,0,4,0,6,0,5,0,5,3,0]))      

    