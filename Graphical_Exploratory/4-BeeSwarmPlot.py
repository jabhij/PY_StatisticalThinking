"""
Instructions --

- In the IPython Shell, inspect the dataframe df using df.head(). This will let you identify which column heading names you need to pass 
as the x and y keyword arguments in your call to sns.swarmplot().
- Use sns.swarmplot() to make a bee swarm plot from the data frame containing the Fisher iris data set, df.
- Label the axes.
- Show your plot.
"""

# Inspect Data Frame
df.head()

# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
