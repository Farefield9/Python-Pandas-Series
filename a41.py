import numpy as np
import pandas as pd
a = ['a','b','c','d']
b = pd.Series([20,33,52,10],a)
c = pd.Series([17,13,31,32],a)
print(b+c)
b = b+c
print(b)
print(b[1:1])
print(b[0:1])
b[0:2] = 12
print(b)
print(b.index,b.values)
