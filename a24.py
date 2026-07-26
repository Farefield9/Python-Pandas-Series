import pandas as pd
import numpy as np
a = pd.Series([2,8,5,3,4,1,7,2,9,6,4])
print(a.sort_values())
print(a.sort_values(ascending=False))
print(a.sort_index())
print(a.sort_index(ascending=False))
