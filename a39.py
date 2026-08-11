import numpy as np
import pandas as pd
a = pd.Series([1,2,3],['a','b','d'])
a[0:3:2] = 5
print(a)
