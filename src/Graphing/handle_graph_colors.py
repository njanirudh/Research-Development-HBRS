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

# File = '/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - fridge.csv'
# File = '/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - drawer.csv'

# File = '/home/jayasimha/NJ/GitHub/Research-Development-HBRS/reports/drawer_handle_grasp - fridge.csv'
File = '/home/jayasimha/NJ/GitHub/Research-Development-HBRS/reports/drawer_handle_grasp - drawer.csv'

with open(File) as csv_file:
    csv_reader = pd.read_csv(csv_file, delimiter=',')
    print(csv_reader.head())
    # print(csv_reader['handle_x'].tolist())

    X_val = np.array(csv_reader['handle_x'].tolist())
    Y_val = np.array(csv_reader['handle_y'].tolist())
    Z_val = np.array(csv_reader['handle_z'].tolist())
    marker = np.array(csv_reader['Success'].tolist())

color_list = ['r' if i == 0 else 'g' for i in marker]
print(color_list)

# OUR ONE LINER ADDED HERE:
# ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([5*0.2401273885350323, 1.0, 5*0.04, 1.]))

ax.scatter(X_val, Y_val, Z_val,color=color_list)
ax.set_xlabel('X Distance - meters')
ax.set_ylabel('Y Distance - meters')
ax.set_zlabel('Z Distance - meters')

plt.show()