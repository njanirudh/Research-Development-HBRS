from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
import pandas
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X_val = []
Y_val = []
Z_val = []

with open('/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - drawer.csv') as csv_file:
# with open('/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - fridge.csv') as csv_file:
    csv_reader = pd.read_csv(csv_file, delimiter=',')
    print(csv_reader.head())
    # print(csv_reader['handle_x'].tolist())

    X_val = np.array(csv_reader['handle_x'].tolist())
    Y_val = np.array(csv_reader['handle_y'].tolist())
    Z_val = np.array(csv_reader['handle_z'].tolist())
    marker = np.array(csv_reader['Success'].tolist())

print(X_val[marker[np.where(marker == 0)]])
marker[np.where(marker == 1)]

color_list = ['r' if i == 0 else 'g' for i in marker]
print(color_list)


ax.scatter(X_val, Y_val, Z_val,color=color_list)
ax.set_xlabel('X Distance - meters')
ax.set_ylabel('Y Distance - meters')
ax.set_zlabel('Z Distance - meters')

plt.show()