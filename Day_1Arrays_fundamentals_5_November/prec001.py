# Find the largest element in an array.

def Largest_ele(arr):
    max_no=arr[0]
    for i in range(1,len(arr)):
        if max_no<arr[i]:
            max_no=arr[i]
    return max_no       

print(Largest_ele([1,6,2,3,8,9,4,5,7,10]))

# Find the second-largest distinct element.

def second_largest(arr):
    unique_arr=[]
    if len(arr)<2:
        return "arr doesnt have 2nd element"

    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    unique_arr=[]
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)  
    return f"second largest elemnt is {arr[2]}"        

print(second_largest([1,6,2,3,8,9,4,5,7,10,10]))

# Reverse an array

def Reverse_of_arr(arr1):
    start=0
    end=len(arr1)-1
    while start<end:
        
        arr1[start],arr1[end]=arr1[end],arr1[start]
        start+=1
        end-=1
    return arr1

        

print(Reverse_of_arr([1,2,3,4,5,6,7,8,9,10]))

# Remove duplicates from a sorted array.

def duplicacy(arr):
    unique_arr=[]
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1], arr[j]

    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)

    return unique_arr

    
        
print(duplicacy([2,6,7,7,3,1,8,9,9]))

   
# Check whether an array is sorted.

def check_sorted(arr):
    

    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
          return "array is sorted " 
        else :
            "array not sorted"
    

        if arr[i]>arr[i+1]:
            return "array is sorted " 
        else :
                    "array not sorted"

print(check_sorted([2,6,7,7,3,1,8,9,9]))


                

       

