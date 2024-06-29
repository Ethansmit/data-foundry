import numpy as np
import pandas as pd
import random as rnd

make = ['Honda', 'Ford', 'Toyota', 'Chevy', 'Kia']
model = ['Element', 'F-150', 'Prius', 'Silverado', 'Forte']
year = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
owners = [0, 1, 2, 3]
condition = ['factory-new', 'used', 'well-used', 'damaged', 'higly-damaged']

# Generate random indices for make and model
n = 10
make_model_indices1 = np.random.choice(len(make), n)

# Generate random data
data1 = {
    'Make': [make[i] for i in make_model_indices1],
    'Model': [model[i] for i in make_model_indices1],
    'Year': np.random.choice(year, n),
    'Owners': np.random.choice(owners, n),
    'Condition': np.random.choice(condition, n)
}

# Create a Pandas dataframe
df1 = pd.DataFrame(data1)
n = 10

make_model_indices2 = np.random.choice(len(make), n)

# Generate random data
data2 = {
    'Make': [make[i] for i in make_model_indices2],
    'Model': [model[i] for i in make_model_indices2],
    'Year': np.random.choice(year, n),
    'Owners': np.random.choice(owners, n),
    'Condition': np.random.choice(condition, n)
}

# Create a Pandas dataframe
df2 = pd.DataFrame(data2)

df3 = pd.concat([df1, df2])

#print(df2.head())
#print(df2.tail(10))
#print(df1.describe())
#print(df1.sort_values(by='Year'))
#print(df1[0:3])
#print(df3['Make'])
#print(df1[df1["Year"] > 2020])