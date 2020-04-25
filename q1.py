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
    x_series = pd.Series(np.random.randint(xlims.min(), xlims.max(), nx))
    y_series = pd.Series(np.random.randint(ylims.min(), ylims.max(), ny))
    c = pd.Series(x_series + 1j * y_series)
    z = c
    for iteration in range(n):
        z = z ** 2 + c
    return pd.DataFrame({'x': x_series, 'y': y_series, 'in_set':(abs(z) < thresh)})


if __name__ == '__main__':
    plt.imshow(mandel(20), )
