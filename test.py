import numpy as np
import pandas as pd

from dataforge import DataForge, Config

#hey = DataForge.generate(DataForge,1,1)
#print(hey)
'''
config = {
    'make': ['Honda', 'Ford', 'Toyota', 'Chevy', 'Kia'],
    'model': ['Element', 'F-150', 'Prius', 'Silverado', 'Forte'],
    'year': [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'owners': [0, 1, 2, 3],
    'condition': ['factory-new', 'used', 'well-used', 'damaged', 'highly-damaged']
}
'''
config = Config()
config.add_attribute('make', ['Honda', 'Ford', 'Toyota', 'Chevy', 'Kia'])
config.add_attribute('model', ['Element', 'F-150', 'Prius', 'Silverado', 'Forte'])
config.add_attribute('year', [2018, 2019, 2020, 2021, 2022, 2023, 2024])
config.add_attribute('owners', [0, 1, 2, 3])
config.add_attribute('condition', ['factory-new', 'used', 'well-used', 'damaged', 'highly-damaged'])


data_generator = DataForge(config)
df = data_generator.generate(10)
print(df)