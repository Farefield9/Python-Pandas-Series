import pandas as pd
import numpy as np
a = pd.Series(data = [1,2,3], index = ['a','b','c'])
print(a.index[1])
print(a.index)
print(a.values)
print(a.dtype)
print(a.shape)
print(a.nbytes)
print(a.ndim)
print(a.size)
print(a.hasnans)
print(a.empty)
print(a.name)
print(a.index.name)
a.index.name = 'Series'
a.name = 'A'
print(a)
print(a[2])
print(a['a'])
