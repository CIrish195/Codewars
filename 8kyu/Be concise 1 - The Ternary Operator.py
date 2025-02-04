#def describe_age(age): 
   # if (age <= 12): 
   #     return "You're a(n) kid"
   # elif (age >= 13 and age <= 17): 
   #     return "You're a(n) teenager"
   # elif (age >= 18 and age <= 64): 
    #    return "You're a(n) adult"
   # else: 
   #     return "You're a(n) elderly"
    
def describe_age(a):
   r="kid"if a<=12else"teenager"if a<= 17else"adult"if a<=64else"elderly";return f"You're a(n) {r}"
