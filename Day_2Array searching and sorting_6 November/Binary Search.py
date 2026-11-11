# Binary Search.
def Binary_Search(arr,num):
    start=0
    end=len(arr)-1
    while start <= end:
            mid=(start+end)//2
        
            if arr[mid]==num:
                return mid

            elif num<arr[mid]:
               end=mid+1

            else:
                 start=mid+1
    # return -1           

print(Binary_Search([1,2,3,4,5,6,7,8,9,10],3))    