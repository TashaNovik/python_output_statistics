import random
import scipy.stats
import numpy as np

random.seed(10)
ages = []
for i in range(0,30):
    n = random.randint(18,75)
    ages.append(n)

ci = scipy.stats.t.interval(0.99, len(ages)-1, loc=np.mean(ages), scale=scipy.stats.sem(ages))
