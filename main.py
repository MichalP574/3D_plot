import matplotlib.pyplot as plt
import numpy as np
import pandas
import openpyxl
from matplotlib import cm

# Website Addresses:
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
# https://matplotlib.org/2.0.2/mpl_toolkits/mplot3d/tutorial.html#surface-plots
# https://matplotlib.org/2.0.2/examples/mplot3d/trisurf3d_demo.html
# https://matplotlib.org/stable/tutorials/colors/colormaps.html

xlsx = pandas.ExcelFile('Example_4_Worksheets.xlsx')

for _ in range(0, 4, 1):
    data = pandas.read_excel(xlsx, _)
    # print(data)
    column_names = [name for name in data.columns]
    X = data[column_names[0]]
    Y = data[column_names[1]]
    Z = data[column_names[2]]

    ax = plt.axes(projection='3d')
    ax.plot_trisurf(X, Y, Z, linewidth=0.2, antialiased=True, cmap='viridis', edgecolor='none')
    plt.xticks(np.arange(min(X), max(X) + 1, 25.0))
    plt.yticks(np.arange(min(X), max(X) + 1, 25.0))
    ax.set_title('Surface Plot')

    ax.set_xlabel(column_names[0])
    ax.set_ylabel(column_names[1])
    ax.set_zlabel(column_names[2])

    plt.show()
