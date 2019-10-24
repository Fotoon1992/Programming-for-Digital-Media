#%%
class MyClass:
    """A simple example class"""
    i = 12345
    def __init__(self, name):
        self.name = name
    def f(self):
        return 'hello world from ' + self.name

#%%
aClass = MyClass("John")
print(aClass.f())
bClass = MyClass("Lucy")
print(bClass.f())

#%%
import json
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
#%% 
with open('out.json','w') as fh:
    json.dump(data, fh)

#%%
# Importing data from a json file:
with open('out.json', 'r') as nfh:
    obj = json.load(nfh)
    print(obj)
    print(obj["president"]["name"])

#%%
from PIL import Image

#%%
mode = 'RGBA'
size = (100, 100)
#olor = 'black'
color = (100, 255, 100, 255)
ourimage = Image.new(mode, size, color)
ourimage

#%%
ourimage.save('allblackinclass.png')

#%%
ourimage.save('allgreeninclass.png')

#%%
ourimage.save('alllightgreeninclass.png')

#%%
#put pixels 
for x in range(ourimage.size[0]):
    for y in range(ourimage.size[1]):
        ourimage.putpixel((x, 50), (255, 255, 255, 255))
ourimage
#%%
ourimage.putpixel((49, 50), (0, 0, 0, 255))
ourimage.putpixel((50, 50), (255, 255, 255, 255))
ourimage.putpixel((51, 50), (0, 0, 0, 255))
ourimage

#%%
#get pixels
ourimage.getpixel((59, 50))

#%%
#colors dots
import random
for x in range(ourimage.size[0]):
    for y in range(ourimage.size[1]):
        value1 = random.randint(0, 255)
        value2 = random.randint(0, 255)
        value3 = random.randint(0, 255)
        ourimage.putpixel((x, y), (value1, value2, value3))
ourimage
#%%
#put line
for x in range(ourimage.size[0]):
        ourimage.putpixel((x, 50), (255, 255, 255, 255))
ourimage
#%%
#grad and shade .. you can change x x x to x y x or y x y
#the color will change with colorful shadows
for x in range(ourimage.size[0]):
    for y in range(ourimage.size[1]):
         ourimage.putpixel((x, y), (x, x, x, 255))
ourimage
#%%
