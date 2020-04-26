import pathlib

import pandas as pd


def largest_species(fname: pathlib.Path = "populations.txt") -> pd.Series:
    """Returns the name of the most widespread species per year.

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    largest_by_year : pd.Series
        Name of most common species per year
    """
    file = pathlib.Path(str(fname))
    if not file.exists():
        raise ValueError(f"File {file} doesn't exist.")
    data = pd.read_table(file)
    # pop the year column since it can mess up the results
    data.pop('# year')
    final_data = data.idxmax(1)
    return final_data

# if __name__ == '__main__':
#  print(largest_species())
