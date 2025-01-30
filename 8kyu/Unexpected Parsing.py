#Orginal Problem



#def get_status(is_busy):
   # status = "busy" if is_busy else "available"      
   # return status

#Solution 

def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return {"status" : status}

# returning status alone only returned a string not the dictionary, to solve the return should be formatted as a dictionary 
# with "status" as the key and the variable status as the value. 
