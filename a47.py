import numpy as np
import pandas as pd
a = pd.Series([1,2,3],['a','b','c'])
print(a*a)
a[0:2] = 10
print(a)
a[2]=0
print(a)
