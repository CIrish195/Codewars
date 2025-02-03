def calculate_tip(amount, rating):
    tip_rate_dict = {
        "terrible" : 0,                  #Create dictionary assigning each rating a tip percentage number
        "poor" : 5,
        "good" : 10,
        "great": 15,
        "excellent" : 20,
    }
    rating = rating.lower()              # make rating lower case so random capitalising is delt with
    if rating in tip_rate_dict:          #check if rating is in dictionary    
        tip = tip_rate_dict.get(rating)  # Get the rating value from dictionary 
        
        result = ((tip * amount) / 100)  # calculate the percentage of tip from amount 
        result = int(round(result+0.5))  # round up the result 
        print (result)
        return result                    # return result
    else:
        return "Rating not recognised"   # if rating isnt in dictionary return "rating not recognised"
