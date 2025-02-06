def no_boring_zeros(n):
    n = str(n)                                  #Convert n to string 
    for i in n:                                 #go through string
        if n[-1] != "0":                        # if the last character isnt 0 
            return int(n)                       #return the number as is as an int 
        elif n == "0":                          # if the number is zero return 0
            return int(0)
        else:
            zero_trail = (n.rstrip("0"))        #otherwise strip the 0s from the end
            return int(zero_trail)              # return result as an int 
