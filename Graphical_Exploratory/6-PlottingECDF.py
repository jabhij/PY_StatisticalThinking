"""
Instructions --

- Use ecdf() to compute the ECDF of versicolor_petal_length. Unpack the output into x_vers and y_vers.
- Plot the ECDF as dots. Remember to include marker = '.' and linestyle = 'none' as arguments inside plt.plot(). Assign the result to _.
- Set the margins of the plot with plt.margins() so that no data points are cut off. Use a 2% margin. Like plt.show() and plt.draw(), the 
plt.margins() does not need to be assigned to _.
- Label the axes. You can label the y-axis 'ECDF'.
- Show your plot.
"""

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle='none')

# Make the margins nice
plt.margins(.02)

# Label the axes
plt.xlabel('ABC')
plt.ylabel('ECDF')

# Display the plot
plt.show()
