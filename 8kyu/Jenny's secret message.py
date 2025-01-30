  #Original Problem 
#def greet(name):
    #return "Hello, {name}!".format(name=name)
    #if name == "Johnny":
        #return "Hello, my love!"

  #Solution 

def greet(name):
    if name != "Johnny":
        return f"Hello, {name}!"
    else:
        return "Hello, my love!"
      
#return with the name was made before checking if the name was johnny.
# makes more sense to to check if the name is johnny and then return the correct string using an if & else statement.
#there was no f string in the first return. I think using the <f"Hello, {name}!"> looks nicer. 

