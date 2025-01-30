def descending_order(num):
    number = str(num)                       #Convert int into string
    list = []                               #create an empty list to store string numbers     
    for i in number:                         
        list.append(i)                      #add each string number to list
        
    list.sort(reverse = True)               #sort list and reverse order                          
    result = " ".join(list)                 #join list to single string 
    return int(result.replace(" ",""))      #return list as an int, with whitespace removed.
