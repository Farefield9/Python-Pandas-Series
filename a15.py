import pandas as pd
import numpy as np
a = np.arange(9,13)
b = pd.Series(index = [1,2,3,4],data = a*2)
print(b)
