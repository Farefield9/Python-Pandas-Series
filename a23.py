import pandas as pd
import numpy as np
a = pd.Series([1,2])
b = pd.Series([3,4])
c = a+b
print(c)
d = a/b
print(d)
print(a[a>1])
