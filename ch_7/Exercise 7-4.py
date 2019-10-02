#%%
def fact(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("Number value is below zero.")
    else:
        return n * fact(n-1)

#%%
def factorial(n):
    answer = 1
    for num in range(1, n+1):
        answer = answer * num
    return answer
    for num in range(1, n-1):
        raise ValueError("Number value is below zero.")

#%%
