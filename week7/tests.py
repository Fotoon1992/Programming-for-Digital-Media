#%%
def factorial(input):
    if(type(input)==type(3.0)):
        raise ValueError("Need an integer value")
       # can use this too print("Bad input")
    if(input==0):
        return 1
    else:
        return input*factorial(input-1)

factorial(10)