#%%
l = [7, 4, 6, 2]

#%%
for num in l:
    print(num)

#%%
for num in l:
    print(num * 2)
    
#%%
def mean (sequence):
    total = 0
    for element in sequence:
        total = total + element
    return total / len(sequence)

#%%
