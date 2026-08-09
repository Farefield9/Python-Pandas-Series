import numpy as np
import pandas as pd
a = pd.Series([1,2,3,4],['a','b','c','d'])
a.rename({'a':'l','b':'m','c':'n','d':'s'},inplace = True)
print(a)
