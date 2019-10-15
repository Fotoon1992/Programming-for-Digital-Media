#%%
#[9.4] Finding the Percentage of Quoted Text
#%%
source = open('pg1342-0.txt', encoding="utf8")
pride = source.read()
print(pride[:1000])

#%%
import re

#%%
result = re.findall(r'[aeiou]', pride)

#%%
len(result)

#%%
result = re.findall(r'[aeiouAEIOU]', pride)

#%%
result

#%%
result[:20]

#%%
quotes = re.findall(r'“[^”]*”', pride)

#%%
len(quotes)

#%%
quotes[:10]

#%%
len(''.join(quotes))

#%%
len(''.join(quotes)) / len(pride)

#%%
(len(''.join(quotes)) / float(len(pride))) * 100

#%%
pride_percent = (len(''.join(quotes)) / float(len(pride))) * 100

#%%
source = open('pg1322-0.txt', encoding="utf8")
leaves = source.read()
leaves[:1000]

#%%
quotes = re.findall(r'“[^”]*”', leaves)
leaves_percent = (len(''.join(quotes)) / float (len(leaves))) * 100
#%%
#[9.5] Counting Words with Regular Expressions
#%%
pride_words = pride.split()

#%%
len(pride_words)

#%%
pride_words_2 = re.findall(r'[A-Za-z]+', pride)
len(pride_words_2)

#%%
pride_words_2[4000:4050]
#%%
#[9.6] Verifying Palindromes—This Time, with Feeling
#%%
test = 'Here is a nice string. La la la.'
re.sub(r'\W+', '', test)

#%%
def prep(text):
    return re.sub(r'\W+', '', text)

#%%
palindrome = 'Star comedy by Democrats.'
print(prep(palindrome))

#%%
otherwise = "This is almost a palindrome ... er, actually it's not."
print(prep(otherwise))

#%%
