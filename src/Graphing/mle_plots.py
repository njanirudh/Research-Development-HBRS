import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
# # Density Plot and Histogram of data samples:
# sns.distplot(samples, hist=True, kde=True,
#              bins=None, color = 'darkblue',
#              hist_kws={'edgecolor':'black'},
#              kde_kws={'linewidth': 4},
#              label='Posterior (Fitted Gaussian)')

# uniform_samples = np.random.uniform(low=x_lim[0], high=x_lim[1], size=num_samples)
uniform_samples = np.random.uniform(low=0.6, high=0.8, size=100000)

sns.distplot(uniform_samples, hist=True, kde=True,
             bins=100, color = 'green',
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 1},
            label='Prior (Uniform)')

plt.title('Distribution of Grasp Pose - X')
plt.xlabel('x-coordinate (m)')
plt.ylabel('Density (%)')
plt.legend()
plt.show()