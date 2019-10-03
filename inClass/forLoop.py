#%%
sum = 0
secondSum = 0
for x in range(100):
    sum = sum + x
    secondSum = secondSum + x * x
#%%
def double(input):
    for x in input:
        print(x*2)

#%%
def exponent(x, y):
    z = x
    for z in range(1, y):
        z = z * x
        return z

#%%
exponent(5, 3)