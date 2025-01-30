def sp_eng(sentence): 
    word = "ENGLISH"               #set word im looking for to ENGLISH
    result = sentence.upper()      #turn sentence all upper case to match word
    if word in result:             # if word is in result return true
        return True
    else:                          # if not return false 
        return False
    pass
