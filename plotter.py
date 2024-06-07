# import matplotlib.pyplot as plt
#
# plt.plot([91.9, 92.5, 94.9, 95.2, 95.05])
# plt.show()
import math

import matplotlib.pyplot as plt
import numpy as np


def get_confidence_interval(p):
    rho = 1.96 * math.sqrt((p * (1 - p)) / 2000)
    return round(p - rho, 4), round(p + rho, 4)


# Data for plotting
fig, ax = plt.subplots()
data = [91.9, 92.5, 94.9, 95.2, 95.05, 96.6]
labels = ['1280/320', '2560/640', '3840/960', '5120/1280', '6400/1600', '6400/1600/e22']
ax.plot(labels,        data)
# plot the confidence intervals
confidence_intervals = np.array([get_confidence_interval(x) for x in np.array(data) / 100])
for i in range(len(data)):
    ax.vlines(x=labels[i], ymin=confidence_intervals[i][0] * 100, ymax=confidence_intervals[i][1] * 100, color='red', alpha=0.7, linewidth=2)
ax.set(xlabel='AI Models Trained/Validated', ylabel='Accuracy in %',
       title='Accuracy of different AI Models')

ax.grid()

# fig.savefig("test.png")

# plt.legend()
ax.legend(loc='upper left', labels=['Accuracy', 'Confidence Interval'])
plt.show()
