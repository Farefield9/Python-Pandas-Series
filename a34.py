import numpy as np
import pandas as pd
a = {1:'a',2:'b'}
b = pd.Series(a)
print(b)
b.rename({2:'c'})
print(b)
print(b.rename({2:'c'}))
b.rename({2:'c'}, inplace = True)
print(b)
print(b.count())
print(b*2)
