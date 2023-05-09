from matplotlib import pyplot as plt
from matplotlib import image
import numpy as np


def zoom(img: np.ndarray) -> np.ndarray:
    '''a function which cuts a picture to zoom in on a specific area

    the values chosen here are random.
    The result is returned.'''
    return img[100:500, 500:800,]


def ft_rotate(img: np.ndarray) -> None:
    '''This is a simple function which calls np.T method to transpose the image.

    It prints the old and new shape and data and then returns the result.'''
    img = zoom(img)
    print("The shape of image is:", img.shape)
    print(img)
    img = np.transpose(img, axes=(1, 0, 2))
    print("New shape after Transpose:", img.shape)
    return img


def main():
    img = image.imread('animal.jpeg')
    img = ft_rotate(img)
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main()
