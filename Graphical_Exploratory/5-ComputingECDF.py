"""
Instructions --

- Define a function with the signature ecdf(data). Within the function definition,
- Compute the number of data points, n, using the len() function.
- The xx-values are the sorted data. Use the np.sort() function to perform the sorting.
- The yy data of the ECDF go from 1/n to 1 in equally spaced increments. You can construct this using np.arange() and then dividing by n.
- The function returns the values x and y.
"""

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y
