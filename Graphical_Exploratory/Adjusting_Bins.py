"""
Instructions --

- Import NumPy as np. This gives access to the square root function, np.sqrt().
- Determine how many data points you have using len().
- Compute the number of bins using the square root rule.
- Be sure to convert the number of bins to an integer.
- Generate the histogram and make sure to use the bins keyword argument and assign the result to _.
- Hit submit to plot the figure and see the fruit of your labors!
"""

# Import NumPy
import numpy as np

# Compute number of data: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot the histogram
_ = plt.hist(versicolor_petal_length, bins=n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()
