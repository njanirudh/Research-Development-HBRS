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

with open("/home/jayasimha/NJ/GitHub/Research-Development-HBRS/reports/drawer_handle_grasp - fridge.csv") as csv_file:
# with open('/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - fridge.csv') as csv_file:
    csv_reader = pd.read_csv(csv_file, delimiter=',')
    print(csv_reader.head())
    # print(csv_reader['handle_x'].tolist())

    X_val = np.array(csv_reader['handle_x'].tolist())
    Y_val = np.array(csv_reader['handle_y'].tolist())
    Z_val = np.array(csv_reader['handle_z'].tolist())
    marker = np.array(csv_reader['Success'].tolist())
