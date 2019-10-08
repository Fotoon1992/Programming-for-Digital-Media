#%%
wyatt = 'They flee from me that sometime did me seek / With naked foot, stalking in my chamber.'
#%%
wyatt = wyatt.lower()
#%%
def twin(pairs):
    pairs = 0
    for i in range(len(wyatt)-1):
        if wyatt[i] == wyatt[i+1]:
            pairs = pairs + 1
    return pairs
#%%
