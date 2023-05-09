import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def ft_grey(img: np.ndarray) -> np.ndarray:
    '''This function applies a grey filter to the image passed by making
    all values of a pixel the same.'''
    arr = np.copy(img)
    vals = np.sum(arr, axis=2) / 3
    arr[:, :, 0] = vals
    arr[:, :, 1] = vals
    arr[:, :, 2] = vals
    return arr


# test
img = ft_load('landscape.jpeg')
img = ft_grey(img)
plt.imshow(img)
plt.show()
