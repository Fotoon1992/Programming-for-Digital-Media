#%%
#for this program, I used the if condition to create a dictionary that has three different terms that are translated into Arabic with their pronunciation. I was trying to modify this code:
def sign(num):
    answer = '?'
    if num > 0:
        answer = '+'
    if num < 0:
        answer = '-'
    if num == 0:
        answer = ''
    return answer 
#instead of using it for positive and negative numbers, I used it to create a small dictionary that was inspired by using Google Translator. I always think of how those things work, and I am guessing that this is a beginner way to make a translator.
#%%
def dictionary(term):
    if term == 'hello world':
        return 'مرحباً بالعالم pronunciation: marhabaan bialealam'
    if term == 'how are you?':
        return 'كيف حالك؟ pronounciation: kayf halik'
    if term == 'see you later!':
        return 'أراك لاحقاً pronunciation: arak lahiqaan'
    else:
        return 'Not defined in this dictionary'
#%%
#The following code works! But this is not how I wanted it to be. I was trying to use for___in___: but I couldn't figure how to make it act accurately. I tried the following ways, and none of them worked:
#1
def age(birth_year):
    today_year = 2019
    for value in birth_year:
        today_age = today_year - value
    return str(today_age) + ' years old!'
#2
def age(birth_year):
    today_age = 0
    for element in birth_year:
        today_age = 2019 - element
    return str(today_age) + ' years old!'
# every time I run this, it gives me ('int' object is not interable). I didn't know what does this means, but I hope you can give me feedback on how to make this program works in a different way of the following one: the only one that works. 

#%%
def age(birth_year):
    today_year = 2019
    today_age = today_year - birth_year
    return str(today_age) + ' years old!'