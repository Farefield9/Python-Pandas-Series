import numpy as np
import pandas as pd
a = pd.Series([654,64,465,5,4,4,65,564,6,452,69,45,65,5,])
a.sort_values()
print(a.sort_values().tail(3))
print(a[a>100])
