from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cbook import get_sample_data
from matplotlib._png import read_png
import matplotlib.pyplot as plt
import numpy as np
import pandas
import pandas as pd
import sklearn.preprocessing as preproc

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X_val = []
Y_val = []
Z_val = []

# with open('/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - drawer.csv') as csv_file:
with open('/reports/drawer_handle_grasp - fridge.csv') as csv_file:
    csv_reader = pd.read_csv(csv_file, delimiter=',')
    # print(csv_reader.head())
    # print(csv_reader['handle_x'].tolist())

    X_val = csv_reader['handle_x'].tolist()
    Y_val = csv_reader['handle_y'].tolist()
    Z_val = csv_reader['handle_z'].tolist()
    marker = np.array(csv_reader['Success'].tolist())

# marker[np.where(marker == 0)] = 'red'
# marker[np.where(marker == 1)] = 'green'

color_list = ['r' if i == 0 else 'g' for i in marker]
# print(color_list)

#------------------------------------------------------

fn = get_sample_data("/home/nj/HBRS/RnD/Research-Development-HBRS/images/frcnn.png", asfileobj=False)
img = read_png(fn)
x_lim, y_lim = ogrid[0:img.shape[0], 0:img.shape[1]]
# lower_x, upper_x = min(X_val),max(X_val)
# x_norm = np.array([lower_x + (upper_x - lower_x) * x for x in x_lim])
y_norm = preproc.minmax_scale(x_lim,(min(Y_val),max(Y_val)))
z_norm = preproc.minmax_scale(np.array(y_lim).T,(min(Z_val),max(Z_val)))
# print(min(y_norm),max(y_norm))
# print(min(Z_val),max(Z_val))
# print(z_norm)

ax = gca(projection='3d')
ax.plot_surface(np.atleast_2d(0.80), y_norm, z_norm.T, rstride=10, cstride=10, facecolors=img)

#------------------------------------------------------

ax.scatter(X_val, Y_val, Z_val,color=color_list)
ax.set_xlabel('X Distance - meters')
ax.set_ylabel('Y Distance - meters')
ax.set_zlabel('Z Distance - meters')

plt.show()
