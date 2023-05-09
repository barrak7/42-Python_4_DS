from load_image import ft_load
import numpy as np
from matplotlib import pyplot as plt


def ft_invert(img: np.ndarray) -> np.ndarray:
    '''A simple function which inverts an image by inverting it's pixel values'''
    return 255 - img


# test
ft_invert(ft_load('landscape.jpeg'))
