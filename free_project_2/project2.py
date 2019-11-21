#%%
img = Image.open('images.png')
# %%
#[Free Project 11-1] Image Manipulation as You Like It:
from PIL import Image 
img = Image.open('free_project_2/images.png')
def pixelize(img):
    new_size = (20, 20)
    connect = Image.BILINEAR
    imgpix = img.resize(new_size, connect)
    result = imgpix.resize(img.size, Image.NEAREST)
    return result
pixelize(img)
#pixelize(img).save('free_project_2/img_pixelize.png')
#%%
