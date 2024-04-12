# ValueError: No axis named X for object type DataFrame

import pandas as pd

df = pd.DataFrame({
    'Animal': ['Cat', 'Cat', 'Cat', 'Dog', 'Dog', 'Dog'],
    'Max Speed': [25, 25, 40, 45, 45, 65]
})

# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f40c1f8d2a0>
print(df.groupby(['Animal', 'Max Speed']))

print('-' * 50)

# Animal  Max Speed
# Cat     25           2
#         40           1
# Dog     45           2
#         65           1
# Name: Animal, dtype: int64
print(df.groupby(['Animal', 'Max Speed'])['Animal'].count())