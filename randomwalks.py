import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
all_walks = []
for i in range(50):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]
count = 0
for i in ends:
    if i >= 60:
        count = count + 1

plt.plot(np_aw_t)
plt.xlabel("Dice rolls --->")
plt.ylabel("Steps --->")
plt.show()

plt.clf()
print("Probability of reaching 60 steps or above = ", str(count)+"%")

# Plot histogram of ends, display plot
plt.hist(ends)
plt.xlabel("Final number of steps reached --->")
plt.ylabel("Frequency --->")
plt.show()
