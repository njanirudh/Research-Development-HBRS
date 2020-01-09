import numpy as np
import pandas
import pandas as pd
import sklearn.preprocessing as preproc
import matplotlib.pyplot as plt

fig = plt.figure()

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

    X_val = csv_reader['handle_x'].tolist()
    Y_val = csv_reader['handle_y'].tolist()
    Z_val = csv_reader['handle_z'].tolist()
    success = np.array(csv_reader['Success'].tolist())

print(min(X_val),max(X_val))
print(min(Y_val),max(Y_val))
print(min(Z_val),max(Z_val))
