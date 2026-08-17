import numpy as np
import pandas as pd
a = pd.Series([1,2,3],['a','b','c'])
print(a['a':'c'])
print(a.count())
