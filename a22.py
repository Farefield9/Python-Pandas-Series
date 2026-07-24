import pandas as pd
import numpy as np
a = pd.Series([1,2,3,4,5,6])
print(a[0:4:2])
print(a[::-1])
print(a[6:8])
print(a[:3]*10)
a[1] = 10
print(a)
a[2:4] = 70
print(a)
a.index = ['a','b','c',3,'e','f']
print(a)
print(a.head())
print(a.tail())
print(a+2)
print(a>10)
