import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def ft_blue(img: np.ndarray) -> np.ndarray:
    '''This function applies a blue filter to the image passed by making each
    of the red and green pixel values into 0.'''
    arr = np.copy(img)
    arr[:, :, 0] = 0
    arr[:, :, 1] = 0
    return arr


# test
img = ft_load('landscape.jpeg')
img = ft_blue(img)
plt.imshow(img)
plt.show()
