#%%
def flop(pngimage):
    width = pngimage.size[0]
    for y in range(pngimage.size[1]):
        for x in range(width):
            top = pngimage.getpixel((x, y))
            bottom = pngimage.getpixel((width - 1 - y, x))
            pngimage.putpixel((width - 1 - y, x), top)
            pngimage.putpixel((x, y), bottom)


#%%
flop(testimage)
testimage

#%%
