import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def ft_green(img: np.ndarray) -> np.ndarray:
    '''This function applies a green filter to the image passed by making each
    of the red and blue pixel values into 0.'''
    arr = np.copy(img)
    arr[:, :, 0] = 0
    arr[:, :, 2] = 0
    return arr


# test
img = ft_load('landscape.jpeg')
img = ft_green(img)
plt.imshow(img)
plt.show()
