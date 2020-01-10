import numpy as np
import pandas
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

fig = plt.figure()

X_val = []
Y_val = []
Z_val = []

# File = '/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - fridge.csv'
File = '/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - drawer.csv'
# File = '/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - door.csv'

# File = '/home/jayasimha/NJ/GitHub/Research-Development-HBRS/reports/drawer_handle_grasp - fridge.csv'

# with open() as csv_file:
with open(File) as csv_file:
    csv_reader = pd.read_csv(csv_file, delimiter=',')
    print(csv_reader.head())
    # print(csv_reader['handle_x'].tolist())

    X_val = csv_reader['handle_x'].tolist()
    Y_val = csv_reader['handle_y'].tolist()
    Z_val = csv_reader['handle_z'].tolist()
    success = np.array(csv_reader['Success'].tolist())

    # Run for FRIDGE
    failure_x = csv_reader['X - failure'].tolist()
    failure_y = csv_reader['Y - failure'].tolist()
    failure_z = csv_reader['Z - failure'].tolist()



    # # RUN for DRAWER
    # Note = csv_reader['Notes'].tolist()
    # for val in Note:
    #     print(val)
    #     # print(val.find('x - failure'))

    grasp = csv_reader['Grasp'].tolist()
    opening = csv_reader['Opening'].tolist()

# print(Note)

failure_x_weight = [2 if x == 'X' else 1 for x in failure_x]
failure_y_weight = [2 if x == 'Y' else 1 for x in failure_y]
failure_z_weight = [2 if x == 'Z' else 1 for x in failure_z]

grasp_weight = [3 if x=='X' else 1 for x in grasp]
opening_weight = [5 if x=='X' else 1 for x in opening]

failure_x_weighted = np.repeat(X_val, failure_x_weight)
failure_x_weighted = failure_x_weighted[np.isfinite(failure_x_weighted)]

failure_y_weighted = np.repeat(Y_val, failure_y_weight)
failure_y_weighted = failure_y_weighted[np.isfinite(failure_y_weighted)]

failure_z_weighted = np.repeat(Z_val, failure_z_weight)
failure_z_weighted = failure_z_weighted[np.isfinite(failure_z_weighted)]

# # print(np.count_nonzero(failure_x_weight))
# # print(np.count_nonzero(failure_y_weight))
# # print(np.count_nonzero(failure_z_weight))
#
mu_x,sigma_y = norm.fit(failure_x_weighted)
print(mu_x,sigma_y)

mu_y,sigma_y = norm.fit(failure_y_weighted)
print(mu_y,sigma_y )

mu_z,sigma_z  = norm.fit(failure_z_weighted)
print(mu_z,sigma_z )
