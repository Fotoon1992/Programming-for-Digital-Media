#%%
source = open('pg1342-0.txt', encoding="utf8")
pride = source.read()
print(pride[:1000])
#%%
source = open('pg1322-0.txt', encoding="utf8")
leaves = source.read()
leaves[:1000]
#%%
import re
#%%
#for the following two programs, I tried to follow as much as I could of what I understood from the reading and I couldn't get the whole term to be appeared but only the last character that follows by !
#%%
exclamation = re.findall(r'.!+', pride)
print(exclamation)
print(len(exclamation))
#%%
exclamation = re.findall(r'.!+', leaves)
print(exclamation)
print(len(exclamation))
#%%
def exc(text):
    return re.findall(r'.!+', text)
#%%
#for the following function I used * to print the whole sentence that follows by ! however this function didn't work well with the above pg texts, it gave a different count of !
#%%
def exc(text):
    return re.findall(r'.*!+', text)