import numpy as np
import pandas
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

def obtain_sample(path):

    X_val = []
    Y_val = []
    Z_val = []

    # with open() as csv_file:
    with open(File) as csv_file:
        csv_reader = pd.read_csv(csv_file, delimiter=',')
        print(csv_reader.head())

        X_val = np.array(csv_reader['grasp_x'].tolist())
        X_val = X_val - np.mean(np.array(csv_reader['handle_x'].tolist()))

        Y_val = np.array(csv_reader['grasp_y'].tolist())
        Y_val = Y_val - np.mean(np.array(csv_reader['handle_y'].tolist()))

        Z_val = np.array(csv_reader['grasp_z'].tolist())
        Z_val = Z_val - np.mean(np.array(csv_reader['handle_z'].tolist()))

        success = np.array(csv_reader['Success'].tolist())

        failure_x = np.array(csv_reader['X - failure'].tolist())
        failure_y = np.array(csv_reader['Y - failure'].tolist())
        failure_z = np.array(csv_reader['Z - failure'].tolist())

        grasp = csv_reader['Grasp'].tolist()
        opening = csv_reader['Opening'].tolist()

    grasp_weight =   [2 if i == 'X' else 0 for  i in grasp]
    opening_weight = [3 if i == 'X' else 0 for  i in opening]

    failure_x_weight = [0 if i == 'X' else 2 for i in failure_x]
    failure_x_weight = np.array(failure_x_weight) + np.array(grasp_weight) + np.array(opening_weight)

    failure_y_weight = [0 if i == 'X' else 2 for i in failure_y]
    failure_y_weight = np.array(failure_y_weight) + np.array(grasp_weight) + np.array(opening_weight)

    failure_z_weight = [0 if i == 'X' else 2 for i in failure_z]
    failure_z_weight = np.array(failure_z_weight) + np.array(grasp_weight) + np.array(opening_weight)

    failure_x_weighted = np.repeat(X_val, failure_x_weight)
    failure_x_weighted = failure_x_weighted[np.isfinite(failure_x_weighted)]

    failure_y_weighted = np.repeat(Y_val, failure_y_weight)
    failure_y_weighted = failure_y_weighted[np.isfinite(failure_y_weighted)]

    failure_z_weighted = np.repeat(Z_val, failure_z_weight)
    failure_z_weighted = failure_z_weighted[np.isfinite(failure_z_weighted)]

    mu_x, sigma_x = norm.fit(failure_x_weighted)
    sample_x = np.random.normal(mu_x, sigma_x, 1)
    print(mu_x, sigma_x)

    mu_y, sigma_y = norm.fit(failure_y_weighted)
    sample_y = np.random.normal(mu_y, sigma_y, 1)
    print(mu_y, sigma_y)

    mu_z, sigma_z = norm.fit(failure_z_weighted)
    sample_z = np.random.normal(mu_z, sigma_z, 1)
    print(mu_z, sigma_z)

    return (sample_x[0],sample_y[0],sample_z[0])

if __name__ == "__main__" :

    # File = '/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - fridge.csv'
    File = '/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - drawer.csv'
    # File = '/home/nj/HBRS/RnD/Research-Development-HBRS/reports/drawer_handle_grasp - door.csv'

    print(obtain_sample(File))