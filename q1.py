import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def mandel(
        n: int,
        thresh: float = 50.0,
        xlims: np.ndarray = np.array([-2, 1]),
        nx: int = 1500,
        ylims: np.ndarray = np.array([-1.5, 1.5]),
        ny: int = 1500,
) -> np.ndarray:
    """Computes the Mandelbrot fractal on some given set of numbers.

    Parameters
    ----------
    n : int
        Number of iterations.
    thresh : float
        Threshold which decides if a number is a part of the set.
    xlims, ylims : np.ndarray
        Limits for the computation of the fractal.
    nx, ny : int
        Number of points between xlims.min() and xlims.max() to calculate the set on.

    Returns
    -------
    img : np.ndarray
        A binary image with a value of 1 if the point belongs to the set.
        The shape of the resulting image is (nx, ny).

    """
    point_df = pd.DataFrame(
        {'x': np.linspace(xlims.min(), xlims.max(), nx), 'y': np.linspace(ylims.min(), ylims.max(), ny)})
    c = pd.Series(point_df['x'] + 1j * point_df['y'])
    z = c
    for iteration in range(n):
        z = z ** 2 + c
        point_df['in_set'] = point_df['y'].apply(lambda z: 1 if abs(z) < thresh else z)
    return point_df



if __name__ == '__main__':
    data = mandel(45)
    print(data)

    plt.imshow(data, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.show()