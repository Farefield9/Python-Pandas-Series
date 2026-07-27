import pandas as pd
import numpy as np
p1 = pd.Series([2, 4, 6, 8, 10])  
p2 = pd.Series([6, 8, 10, 12, 14, 16])  
print(p1[~p1.isin(p2)])
