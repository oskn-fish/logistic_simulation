#%%
import pandas as pd
import random

GENERATIONS = 100
param = 2

gen = random.random()
x = [gen]
for i in range(GENERATIONS):
    next_gen = param*gen*(1-gen)
    x.append(next_gen)
    gen = next_gen
# y = range(GENERATIONS)
x = pd.DataFrame(x)
x.plot()

