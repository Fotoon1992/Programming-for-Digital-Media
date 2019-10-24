#%%
import re
#%%
#
#%%
text = ""
re.search("", text)
#%%
#\d digits
#\w letters
# \d = [0-9] 
# \d = [0123456789]
# ^ begin the string, $ end of string, ? optional, * repeat 0 to more
# + repeat 1 to more, {2} only 2, {2,} 2 or more, | means or
# [1-34-6] means that from 1 to 3 and from 4 to 6
#%%
zipcode1 = "31245"
zipcode2 = "32124-2432"
zipcode3 = "3214"
zipcode4 = "oue23"
#%%
regexp = "^\d{5}(-\d{4})?$"
print(re.search(regexp, zipcode1))
print(re.search(regexp, zipcode2))
print(re.search(regexp, zipcode3))
print(re.search(regexp, zipcode4))
#%%
#time of day
#%%
time0 = "5pm"
time1 = "6am"
time2 = "2:00p"
time3 = "13:00a"
time4 = "00:02am"
#%%
regexp = "^([1-9]|1[0-2])(:\d\d)?[ap]m?$"
print(re.search(regexp, time0))
print(re.search(regexp, time1))
print(re.search(regexp, time2))
print(re.search(regexp, time3))
print(re.search(regexp, time4))

# %%
