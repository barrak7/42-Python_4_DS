from matplotlib import pyplot as plt
from load_csv import load
import pandas as pd
from matplotlib.ticker import MaxNLocator


def aff_life(df: pd.DataFrame) -> None:
    '''Takes a DataFrame and plots it using pyplot'''

    locator = MaxNLocator('auto')
    plt.plot(df.keys(), df, label='Age')
    plt.gca().xaxis.set_major_locator(locator)
    plt.xlabel('Years')
    plt.ylabel('Age')

    plt.title('Morocco life expectancy projection')
    plt.legend()
    plt.show()


def main():
    data = load('life_expectancy_years.csv')
    print(data)
    data = data.set_index('country')
    aff_life(data.loc['Morocco'])


if __name__ == '__main__':
    main()
