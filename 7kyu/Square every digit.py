def square_digits(num):
    list = []                                       #set up list for squared numbers
    for i in str(num):                              #convert numbers to string and itterate through numbers
        i = int(i)                                  # convert each number to int for calculation
        square =(i * i)                             # square each nummber
        list.append(square)                         #add square number on to list 
        int_result = int(''.join(map(str, list)))   #join list together into single int
    return (int_result)
    return(result)
