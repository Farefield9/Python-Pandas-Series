import numpy as np
import pandas as pd
a = pd.Series([1,2,3])
b= a.sort_values(ascending = False)
print(b)
