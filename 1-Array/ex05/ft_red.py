import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def ft_red(img: np.ndarray) -> np.ndarray:
    '''This function applies a red filter to the image passed by making each
    of the green and blue pixel values into 0.'''
    arr = np.copy(img)
    arr[:, :, 1] = 0
    arr[:, :, 2] = 0
    return arr


# test
img = ft_load('landscape.jpeg')
img = ft_red(img)
plt.imshow(img)
plt.show()
