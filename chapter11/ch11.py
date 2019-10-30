#%%
from PIL import Image
#%%
ourimage = Image.open('img.png')
img = ourimage
#%%
ourimage
#%%
around
#%%
around = img.getpixel((x - 1, y - 1))[0] + \
    img.getpixel((x, y - 1))[0] + \
    img.getpixel((x + 1, y - 1))[0] + \
    img.getpixel((x - 1, y))[0] + \
    img.getpixel((x + 1, y))[0] + \
    img.getpixel((x - 1, y + 1))[0] + \
    img.getpixel((x, y + 1))[0] + \
    img.getpixel((x + 1, y + 1))[0]
#around 1529
#%%
around = around / 8
#around 191.125
#%%
ourimage.size
#348, 340

#%%
#darck spot
x, y = (147, 170)
#around 150.5
#%%
#light spot
x, y = (340, 170)
#around 191.125
#%%
around = 0
for c in [0, 1, 2]:
    around = around + \
        img.getpixel((x - 1, y - 1))[c] + \
        img.getpixel((x, y - 1))[c] + \
        img.getpixel((x + 1, y - 1))[c] + \
        img.getpixel((x - 1, y))[c] + \
        img.getpixel((x + 1, y))[c] + \
        img.getpixel((x - 1, y + 1))[c] + \
        img.getpixel((x, y + 1))[c] + \
        img.getpixel((x + 1, y + 1))[c]
#around 2636
#%%
around = around / 24.0
#around 109.83333333333333
#%%
def nearby(img, x, y):
    around = 0
    for c in [0, 1, 2]:
        around = around + \
            img.getpixel((x - 1, y - 1))[c] + \
            img.getpixel((x, y - 1))[c] + \
            img.getpixel((x + 1, y - 1))[c] + \
            img.getpixel((x - 1, y))[c] + \
            img.getpixel((x + 1, y))[c] + \
            img.getpixel((x - 1, y + 1))[c] + \
            img.getpixel((x, y + 1))[c] + \
            img.getpixel((x + 1, y + 1))[c]
    return around / 24.0
print(around)
#109.83333333333333
#%%
def differ(img, x, y):
    current = 0
    around = 0
    for c in [0, 1, 2]:
        current = current + img.getpixel((x, y))[c]
        around = around + \
            img.getpixel((x - 1, y - 1))[c] + \
            img.getpixel((x, y - 1))[c] + \
            img.getpixel((x + 1, y - 1))[c] + \
            img.getpixel((x - 1, y))[c] + \
            img.getpixel((x + 1, y))[c] + \
            img.getpixel((x - 1, y + 1))[c] + \
            img.getpixel((x, y + 1))[c] + \
            img.getpixel((x + 1, y + 1))[c]
    return (around / 24.0) - (current / 3.0)
print(around)
#109.83333333333333
#%%
def blur(img):
    blurred = Image.new('RGB', img.size, 'white')
    for x in range(1, img.size[0] -1):
        for y in range(1, img.size[1] -1):
            (r, g, b, a) = img.getpixel((x, y))
            change = differ(img, x, y) / 2.0
            change = int(round(change))
            blurred.putpixel((x, y), (r + change, g + change, b + change))
    return blurred
#no () between x and y for differ and needed for a
#%%
int(500.2)

#%%
ratio = 120.7

#%%
int(ratio)

#%%
round(ratio)

#%%
type(round(ratio))

#%%
int(round(ratio))

# %%
from PIL import Image
import PIL.ImageOps
#%%
img = Image.open('source.png')
inverted = PIL.ImageOps.invert(img)
inverted.save('inverted.png')

#%%
def invert(img):
    for x in range(225):
        for y in range(225):
            (r, g, b, a) = pngimage.getpixel((x, y))
            pngimage.putpixel((x, y), (r, g, b, a))

