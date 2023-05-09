import numpy as np
from matplotlib import image


def ft_load(path: str) -> np.ndarray:
    '''A function which loads image data and returns it in rgb format.
    '''
    try:
        img = image.imread(path)
    except Exception as e:
        print("Error: couldn't load image:", e)
        return

    print("The shape of the image is:", img.shape)
    return (img[:, :, :3])
