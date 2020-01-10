from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__" :

    FILE_PATH = "/home/nj/Documents/hsr_doorgym/with_collisions/hsr_doorgym_default_ppo_params_single_env.txt"

    x_mean = []
    y_mean = []
    min_value = []
    max_value = []

    f = open(FILE_PATH, "r")
    i = 1
    for line in f:
        if "Last 10 training episodes:" in line:
            i += 10
            x_mean.append(i)
            y_mean.append(float(line.split()[6].split("/")[0]))

            min_value.append(float(line.split()[-1].split("/")[0]))
            max_value.append(float(line.split()[-1].split("/")[1]))
            # print(line.split()[-1].split("/")[0])
            # print(line.split()[9])

    print(x_mean)
    print(y_mean)
    print(min_value)
    print(max_value)

    fig = plt.figure()
    plt.plot(x_mean, y_mean,color='red',label='Mean Reward',linewidth=1)
    # plt.plot(x_mean, max_value,color='blue')
    # plt.plot(x_mean, min_value,color='blue')

    plt.fill_between(x_mean, min_value, max_value ,color='blue', alpha='0.3')
    plt.legend(loc="upper right")
    plt.xlabel('Batch')
    plt.ylabel('Reward')

    plt.show()
