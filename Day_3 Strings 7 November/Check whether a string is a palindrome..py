def check_palindrom(text):
    reversed_str=""
    for char in text:
        reversed_str=char+ reversed_str

    print(reversed_str)    

    if text==reversed_str:
         return "Given String is palindrom"
    else:
        return "Non Palindrom"

      

    #    if text==reversed_str:
    #        return "Given String is palindrom"
    #    else:
    #       return "Non Palindrom"

print(check_palindrom("Harshal"))
 
