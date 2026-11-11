# Two Sum
def Two_Sum(arr,target):
    new_arr=[]
    for i, num in enumerate(arr):
        componante=target-num

    if componante not in new_arr:
        new_arr.append(num)
    return new_arr


    # return new_arr

print(Two_Sum([2,7,11,15],9))


        
   
    
          
           


