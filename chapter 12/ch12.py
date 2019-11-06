#%%
def mean(sequence):
    sum = 0.0
    for element in sequence:
        sum = sum + element
    return sum/len(sequence)
# %%
values = [10, 9, 73, 25, 33, 76, 52, 1, 35, 86]
#%%
#the reading was missing ()
print(mean(values))
# %%
# the code in processing is not working