from PIL import Image
from scipy import ndimage
import numpy as np
from scipy.misc import imread
from scipy.misc import imsave
from skimage import data, io, filters
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import ImageDraw

def rgb2gray(rgb): #from stackoverflow
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def invert(image):
    for x in xrange(0,image.shape[0]):
        for y in xrange(0,image.shape[1]):
            if (image[x][y]>70):
                image[x][y]= 0
            else:
                image[x][y]= 255
    return image

def filter_im(image, sig1, sig2):
    image = filters.sobel(image)
    image = ndimage.gaussian_filter(image,sig1)-ndimage.gaussian_filter(image,sig2)
    image /= np.max(np.abs(image),axis=0)
    image *= (255.0/image.max())
    return image

def connect_points(image, x1, y1, x2, y2):
    img = Image.fromarray(image)
    draw = ImageDraw.Draw(img)
    draw.line((x1,y1,x2,y2),fill=0)
    image = np.asarray(img)
    return image
""" will connect a outer point to the closest point
within a radius, that is not already connected to the point """
def connecter(image, x, y):
    ymax = image.shape[1]
    xmax = image.shape[0]
    for y_add in xrange(20,90):
        for x_add in xrange(20,90):
            if y+y_add < ymax and x+x_add<xmax  and image[x+x_add][y+y_add] == 0:
                return connect_points(image, x, y, x+x_add, y+y_add)
            if y+y_add < ymax and x-x_add>=0  and image[x-x_add][y+y_add] == 0:
                return connect_points(image, x, y, x-x_add, y+y_add)
            if y-y_add  >= 0 and x+x_add<xmax and image[x+x_add][y-y_add ] == 0:
                return connect_points(image, x, y, x+x_add, y-y_add)
            if y-y_add  >= 0 and x-x_add>=0 and image[x-x_add][y-y_add ] == 0:
                return connect_points(image, x, y, x-x_add, y-y_add)

def nearest_have_white(image, x, y):
    if y+1 < image.shape[1] and image[x][y+1] == 255:
        return True
    if y-1 >= 0 and image[x][y-1] == 255:
        return True
    if x+1 < image.shape[0] and image[x+1][y] == 255:
        return True
    if x-1 >= 0 and image[x-1][y] == 255:
        return True

def connect_lines(image):
    for x in xrange(0,image.shape[0],5):
        for y in xrange(0,image.shape[1],5):
            if image[x][y] == 0 and nearest_have_white(image, x, y):
                connecter(image, x, y)
    return image

def thin_lines(image):
    for x in xrange(0,image.shape[0],5):
        for y in xrange(0,image.shape[1],5):
            if image[x][y] == 0 and nearest_have_white(image, x, y):
                image[x][y] = 255
    return image

def image_processing(name, show = 0, connect=0):
    image = Image.open("%s.jpg" %name)
    #image.thumbnail((1200,1200))
    image = np.asarray(image)
    image = rgb2gray(image)#image.convert('1')   #black and white
    image = filter_im(image,1,6)
    image = invert(image)
    if connect:
        image = connect_lines(image)
        image = thin_lines(image)
    if show:
        plt.imshow(image, cmap=cm.gray)
        plt.show()

    """ give image transparency """
    image = Image.fromarray(image)
    image = image.convert("RGBA")
    datas = image.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    image.putdata(newData)

    image.thumbnail((800,800))
    imsave("%s_lineart.png" %(name), image)

#image_processing("buildings", show = 0)
image_processing("tiger",show = 1)
image_processing("cupcake",show = 1)
