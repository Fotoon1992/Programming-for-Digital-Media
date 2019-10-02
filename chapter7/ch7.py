#%%
print('Hello World')

#%%
def to_f(c):
    return ((9/5) * c) + 32

#%%
def to_c(f):
    return (5/9) * (f-32)

#%%
def to_f(c):
    if c < -273.15:
        raise ValueError("Temperature value is below absolute zero.")
        return ((9/5) *c) + 32

#%%
def sign(num):
    answer = '?'
    if num > 0:
        answer = '+'
    if num < 0:
        answer = '-'
    if num == 0:
        answer = ''
    return answer

#%%
def sign(num):
    answer = '?'
    if num > 0:
        answer = '+'
    elif num < 0:
        answer = '-'
    else:
        answer = ''
    return answer
#%%
name = 'Paula'
name[-1]

#%%
word = 'hello'
word[-1]

#%%
'world'[-1]

#%%
def gender(name):
    if name[-1] == 'a':
        return 'female'
    if name[-1] == 'o':
        return 'male'

#%%
def gender(name):
    indicated = '?'
    if name[-1] == 'a':
        indicated = 'female'
    if name[-1] == 'o':
        indicated = 'male'
    return indicated    

#%%
list(range(5))

#%%
list(range(0, 5))

#%%
list(range(1, 6))

#%%
answer = 1
for num in range(1, 6):
    answer = answer * num
answer

#%%
def factorial(n):
    answer = 1
    for num in range(1, n+1):
        answer = answer * num
    return answer
#%%
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

#%%
def doubler(sequence):
    if len(sequence) == 0:
        return []
    else:
        return [2 * sequence[0]] + doubler(sequence[1:])

#%%
