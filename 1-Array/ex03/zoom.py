from load_image import ft_load
from matplotlib import pyplot as plt


def zoom(path: str) -> None:
    img = ft_load(path)
    if img is None:
        return
    print(img)
    img = img[300:500, 100:700, :]
    print("New shape after Slicing:", img.shape)
    plt.imshow(img)
    plt.show()


# test
def main():
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
