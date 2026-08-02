import numpy as np
import pandas as pd
a = pd.Series([1,2,3,4],['b','c','d','e'])
print(a['b':'d']*2)
a[0]='c'
print(a)
print(a._data)
