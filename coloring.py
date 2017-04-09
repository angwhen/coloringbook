from PIL import Image
from scipy import ndimage
import numpy as np
from scipy.misc import imread
from scipy.misc import imsave
from skimage import data, io, filters
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import ImageDraw

name = "cat"
image = Image.open("%s_lineart.png"%name)
image_color = Image.open("%s.jpg"%name)


plt.imshow(image)
plt.show()
