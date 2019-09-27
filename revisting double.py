#%%
volume = [4.0, 2.0, 3.0, 5.5]
result = []
for element in volume:
    result = result + [element * 2]

#%%
def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
        return result

#%%
