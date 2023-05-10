from matplotlib import pyplot as plt
from load_csv import load
import pandas as pd


def project_life(life: pd.DataFrame, gdp: pd.DataFrame):
    '''A function which displays the projection of life expectancy
    in relation to the gross national product of the year 1900.

    It uses matplotlib. None is returned.'''
    plt.scatter(life, gdp)
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')
    plt.show()


def main():
    life = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    gdp = load('life_expectancy_years.csv')
    project_life(life.loc[:, '1900'], gdp.loc[:, '1900'])


if __name__ == '__main__':
    main()
