import pandas as pd
import numpy as np
a = [1,2,3]
b = ['a','b','c']
c = pd.Series(a,b)
print(c)
d = pd.Series(data = a, index = b)
print(d)
