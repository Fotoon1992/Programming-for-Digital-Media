#%%
def set_a():
    a = 10
    print('The value of a:', a)
#%%
 set_a()
#%%
a = 20
print('Initially, the value of a:', a)
set_a()
print('Finally, the value of a:', a)
#%%
def scoped(first, second):
    third = second + second - first
    return third

#%%
first = 10
second = 11
third = 12
scoped(2, 4)

#%%
