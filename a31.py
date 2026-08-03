import numpy as np
import pandas as pd
a = pd.Series([1,2,3])
print(a+2)
print(a*2)
print(a-2)
print(a**2)
print(a/2)
print(a>2)
print(a<2)
print(a[a%2==0])
print(a[a%2!=0])
