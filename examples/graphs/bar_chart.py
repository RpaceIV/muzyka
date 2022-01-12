# Libraries
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.pyplot import figure

# Make a random dataset:
height = [3, 12, 5, 18, 45] #list
bars = ('A', 'B', 'C', 'D', 'E') #tuple

print(type(height))

print(type(bars))

y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
plt.xticks(y_pos, bars)
# figure(figsize=(20, 20), dpi=80)
# Show graphic
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.show()