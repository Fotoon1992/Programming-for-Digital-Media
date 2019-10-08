#%%
def count_nonspaces(a):
    print((len(a)) - (len(a.split(' '))-1))