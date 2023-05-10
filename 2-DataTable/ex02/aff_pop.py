from matplotlib import pyplot as plt
import pandas as pd
from load_csv import load
from matplotlib.ticker import MaxNLocator


def aff_pop(df: pd.DataFrame) -> None:
    '''Function which takes a dataframe and shows the population of my campus against some other campus:

    it plots the data using pyplot. The return value is None.'''
    _, ax = plt.subplots()
    y_locator = MaxNLocator(3)
    x_locator = MaxNLocator(7)
    ax.plot(df.loc['Belgium', '1800':'2050'].keys(),
            df.loc['Belgium', '1800':'2050'], label='Belgium')
    ax.plot(df.loc['France', '1800':'2050'].keys(),
            df.loc['France', '1800':'2050'], label='France')
    ax.set_xlabel('Years')
    ax.set_ylabel('Population')
    ax.set_title('Belgium vs France Populations')
    ax.yaxis.set_major_locator(y_locator)
    ax.xaxis.set_major_locator(x_locator)
    ax.legend(loc='lower right')
    plt.show()


def main():
    data = load('population_total.csv')
    data = data.set_index('country').loc[['Belgium', 'France'], :]
    aff_pop(data)


if __name__ == '__main__':
    main()
