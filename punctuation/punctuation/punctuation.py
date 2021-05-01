def unpunctuate(s) : 
    x=0
    new=0
    counter = len(s)        #Finding the count of chacacters in which 's'.
    punctuations  = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
    for  x in  range(0,counter-1) :
        if s[x]  in punctuations:       #Checking the whole characters either a punctuation or not.
           y = s[x]
           s = s.replace(y , "")      #Replacing the punctuations with 'null' string.
    return s

s = input("Enter the sentence : ")
new = unpunctuate(s)
print(new)


