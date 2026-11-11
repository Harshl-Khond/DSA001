# Check whether two strings are anagrams.
def check_anagram(text1, text2):
    fre1={}
    for char in text1:
        if char.isalpha():
            fre1[char]=fre1.get(char,0)+1
    

    fre2={}
    for char in text2:
            if char.isalpha():
                fre2[char]=fre2.get(char,0)+1

    if fre1==fre2:
         return "anagram"
    else:
         return "non anagram"


print(check_anagram("tnelis","silent"))    
          



