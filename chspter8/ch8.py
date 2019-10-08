#%%
#length of strings
#%%
len('hellp world')

#%%
len('2112')

#%%
len('')

#%%
hi = 'hello world'

#%%
len(hi)

#%%
len("hello world")

#%%
'hello'[0]

#%%
'hello'[1]

#%%
'hello'[5]

#%%
'hello'[4]
#%%
#selecting a slice
#%%
'hello world'[0:3]

#%%
'2112'[0:3]

#%%
''[0:3]

#%%
'hello'[0:1]

#%%
''[0]

#%%
''[0:1]

#%%
'hello world'[0:500]

#%%
'hello world'[450:500]

#%%
'hello world'[:3]

#%%
'hello world'[1:]

#%%
'hello world'[:5]

#%%
'hello world'[6:]

#%%
#upper()
#%%
greeting = 'hello world'

#%%
greeting[0].upper() + greeting[1:]

#%%
#step
#%%
'abcdefgh'[0:9:2]

#%%
'abcdefgh'[::2]

#%%
'0123456789'[::2]

#%%
'hello world'[-1:]

#%%
'hello world'[-5:]

#%%
#counting double letters
#%%
wyatt = 'They flee from me that sometime did me seek / With naked foot, stalking in my chamber.'

#%%
'HELLO world'.lower()


#%%
original = 'Burma Shave'
lowercase = original.lower()

#%%
lowercase

#%%
original

#%%
wyatt = wyatt.lower()

#%%
wyatt

#%%
for c in wyatt:
    print(c)

#%%
for i in range(len(wyatt)):
    print(wyatt[i])

#%%
for i in range(len(wyatt)):
    print(i, wyatt[i])

#%%
range(len(wyatt))

#%%
len(wyatt)

#%%
for i in range(len(wyatt)):
    print wyatt[i:i+2]

#%%
pairs = 0
for i in range(len(wyatt)):
    if wyatt[i:i+2] == 'ee':
        pairs = pairs + 1

#%%
pairs

#%%
#error
pairs = 0
for i in range(len(wyatt)):
    if wyatt[i] == wyatt[i+1]:
        pairs = pairs + 1

#%%
pairs

#%%
wyatt[86]

#%%
pairs = 0
for i in range(len(wyatt)-1):
    if wyatt[i] == wyatt[i+1]:
        pairs = pairs + 1

#%%
pairs

#%%
#strings and their lemgth
#%%
text = 'All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.'

#%%
#number of characters
len(text)

#%%
#splitting a text into words
#%%
text.split(' ')


#%%
#number of words
len(text.split(' '))

#%%
text.split('and')


#%%
hi = 'hello   world'
hi.split(' ')

#%%
'hello  world'.split(' ')

#%%
hi.split()

#%%
# working across strings: poining and sorting
#%%
names = ['Bob', 'Carol', 'Ted', 'Alice']

#%%
' & '.join(names)

#%%
' and/or '.join(names)

#%%
'\n'.join(names)

#%%
print('\n'.join(names))

#%%
#add 'exists' in each spliting line
print(' exists.\n'.join(names))

#%%
#add exisrs after each string because of for----in----:
#each word without joining
for person in names:
    print(person + ' exists.')

#%%
sorted(names)

#%%
names.sort()

#%%
