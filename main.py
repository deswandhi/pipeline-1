import pandas as pd

# create list of columns to use
cols = ['zipcode','agi_stub','mars1','MARS2','NUMDEP' ]

# create data frame from csv using only  selected columns
data = pd.read_csv("dataset/vt_tax_data_2016.csv", usecols=cols)

# View print of dependents and tax returns by income level-2
print (data.groupby('agi_stub').sum())