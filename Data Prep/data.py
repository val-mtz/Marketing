# Created: 21/Feb/2025 - Valeria Martínez (A01782413)
# Modified: 21/Feb/2025 - Valeria Martínez (A01782413)

# This script reads the project's survey database and filters out rows with no GenZ age values.

import pandas as pd

# Open csv file as a dataframe
df = pd.read_csv('base.csv')

# List of all non-GenZ age columns
nonGenZ = ['HASTA_3_AÑOS', 'E_4AÑOS6AÑOS', 'E_7AÑOS12AÑOS', 'E_30AÑOS39AÑOS', 'E_40AÑOS49AÑOS', 'E_50AÑOS59AÑOS' , 'E_60AÑOSYMAS']

# Filter to keep rows where all the non-GenZ values are blank
df = df[df[nonGenZ].isnull().all(axis=1)]

# With the new data set, we now remove the rows where our GenZ values are blank
df = df[df['E_13AÑOS19AÑOS'].notnull() | df['E_20AÑOS29AÑOS'].notnull()]

# The two steps above can be done at once, like so:
# df = df[df[nonGenZ].isnull().all(axis=1) & (df['E_13AÑOS19AÑOS'].notnull() | df['E_20AÑOS29AÑOS'].notnull())]

# Finally, to compare the accuracy against our Excel process, we print the number of rows in the new data set
print(f"Total rows in new dataset: {len(df)}")