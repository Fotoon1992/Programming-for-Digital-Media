#%%
twod = (42, 17)

#%%
threed = (7, 6, 14)

#%%
#doesn't work since it is tuple
threed[0] = 8

#%%
alist = [1, 2, 3]

#%%
alist[0] = 17

#%%
for i in range(5):
    print((i, 2, 3))

#%%
def to_f(c):
    return ((9/5) * c) + 32

#%%
to_f('hello')

#%%
def double(threed):
    result = (2, 3, 4)
    for element in threed:
        result = result + [element * 2]
        return result

#%%
from PIL import Image

#%%
ourimage = Image.new('RGBA', (100, 100), 'black')

#%%
#call the image we have built
ourimage

#%%
mode = 'RGBA'
size = (100, 100)
color = 'black'
ourimage = Image.new(mode, size, color)

#%%
ourimage

#%%
#way to save the image
ourimage.save('allblack.png')

#%%
help(len)

#%%
help(Image)

#%%
help(Image.new)

#%%
#docstring
def tax(subtotal):
    "Return the amount of detective tax due on the given subtotal."
    return subtotal * 0.08875

#%%
dir([])

#%%
help([].count)

#%%
ourimage = Image.new('RGBA', (100, 100), (127, 127, 127, 255))

#%%
ourimage.save('allgray.png')

#%%
ourimage = Image.new('RGBA', (100, 100), (200, 127, 127, 255))

#%%
ourimage.save('allrose.png')

#%%
allblack = Image.new('RGB', (100, 100), (0, 0, 0, 255))

#%%
allblack = Image.new('RGB', (100, 100))

#%%
allblack.putpixel((50, 50), (255, 255, 255, 255))

#%%
allblack.save('almostall.png')
#%%
#create a line image.
#%%
allblack = Image.new('RGB', (100, 100))
for x in range(100):
    for y in range(4):
        allblack.putpixel((x, y), (255, 255, 255, 255))
#%%
allblack
#%%
allblack.save('oneline.png')
#%%
#rectangle
#%%
rectangle = Image.new('RGB', (150, 100))

#%%
rectangle

#%%
for x in range(150):
    for y in range(100):
        rectangle.putpixel((x, y), (127, 127, 127, 255))

#%%
rectangle
#%%
#shadow
#%%
for x in range(150):
    for y in range(100):
        rectangle.putpixel((x, y), (x, x, x))

#%%
rectangle.save('gradient.png')

#%%
def redness(square):
    all_red = 0;
    others = 0;
    for x in range(100):
        for y in range(100):
            red, green, blue, alpha = square.getpixel((x, y))
            all_red = all_red + red
            others = others + green + blue
    return all_red - (others / 2)

#%%
rectangle.size

#%%
bigger = Image.new('RGB', (500, 600), (0, 0, 0, 255))

#%%
bigger.size

#%%
bigger.size[0]

#%%
bigger.size[1]

#%%
def grayout(pngimage):
    for x in range(225):
        for y in range(225):
            pngimage.putpixel((x, y), (127, 127, 127, 255))

#%%
test = Image.new('RGB', (150, 100))

#%%
grayout(test)

#%%
test

#%%
test.save('grayout_test.png')

#%%
ourimage = Image.open('example1.png')

#%%
ourimage

#%%
grayout(ourimage)

#%%
ourimage

#%%
ourimage.size
#values for the range functions!!!!! important
#225, 225 example.png
#310, 308 example1.png
#%%
ourimage.getpixel((0, 0))
#(8, 4, 3)
#%%
def modify(pngimage):
    for x in range(225):
        for y in range(225):
            (r, g, b, a) = pngimage.getpixel((x, y))
            pngimage.putpixel((x, y), (r, g, b, a))

#%%
#doesn't work
pangimage.putpixel((x, y), (r +64, g + 64, b + 64,a))

#%%
#set brightness
# to set the colors not to be more than 225 or less than 0
#%%
def modify(pngimage):
    for x in range(310):
        for y in range(308):
            (r, g, b) = pngimage.getpixel((x, y))[:3]
            new_color = (r + 64, g + 64, b + 64)
            new_color = new_color + pngimage.getpixel((x, y))[:3]
            pngimage.putpixel((x, y), new_color)

#%%
ourimage

#%%
modify(ourimage)

#%%
#set darkness function
#%%
def darken(pngimage):
    for x in range(225):
        for y in range(225):
            (r, g, b) = pngimage.getpixel((x, y))[:3]
            new_color = (r - 64, g - 64, b - 64)
            new_color = new_color + pngimage.getpixel((x, y))[:3]
            pngimage.putpixel((x, y), new_color)

#%%
darken(ourimage)

#%%
ourimage = Image.open('example1.png')
#%%
#255+255+255 = 382.5
#%%
def contrast(pngimage):
    for x in range(310):
        for y in range(308):
            (r, g, b) = pngimage.getpixel((x, y))[:3]
            new_color = (r + 64, g + 64, b + 64)
            new_color = new_color + pngimage.getpixel((x, y))[:3]
            if r + g + b < 382.5:
                pngimage.putpixel((x, y), (r - 64, g - 64, b - 64))
            else:
                pngimage.putpixel((x, y), (r + 64, g + 64, b + 64))


#%%
contrast(ourimage)

#%%
ourimage
#%%
# flip numbers in two variables
#%%
a = 17
b = 2

#%%
temp = a
a = b
b = temp

#%%
(a, b)


#%%
def flip(pngimage):
    width = pngimage.size[0]
    for y in range(pngimage.size[1]):
        for x in range(width):
            left = pngimage.getpixel((x, y))
            right = pngimage.getpixel((width - 1 - x, y))
            pngimage.putpixel((width - 1 - x, y), left)
            pngimage.putpixel((x, y), right)

#%%
testimage = Image.open('flipme.png')
flip(testimage)
testimage

#%%
