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
config.add_attribute('model', ['Element', 'F-150', 'Prius', 'Silverado', 'Forte', 'Stinger'])
config.add_attribute('year', [2018, 2019, 2020, 2021, 2022, 2023, 2024])
config.add_attribute('condition', ['factory-new', 'used', 'well-used', 'damaged', 'highly-damaged'])
config.add_attribute('owners', [0, 1, 2, 3])

# Adding dependency for 'model' based on 'make'
make_model_mapping = {
    'Honda': ['Element'],
    'Ford': ['F-150'],
    'Toyota': ['Prius'],
    'Chevy': ['Silverado'],
    'Kia': ['Forte', 'Stinger']
}

year_condition_mapping = {
    2018 : ['well-used','damaged','highly-damaged'],
    2019 : ['well-used','damaged','highly-damaged'],
    2020 : ['well-used','damaged','highly-damaged'],
    2021 : ['used', 'well-used'],
    2022 : ['used', 'well-used'],
    2023 : ['factory-new', 'used', 'well-used'],
    2024 : ['factory-new']
}

condition_owner_mapping = {
    'factory-new' : [0],
    'used' : [1, 2],
    'well-used' : [1, 2, 3],
    'damaged' : [2, 3],
    'highly-damaged' : [3]
}
'''
make_model_year_mapping = {
    ('Ford', 'F-150'): [2019, 2020],
    ('Honda', 'Element'): [2020, 2021],
    ('Toyota', 'Prius'): [2022, 2023],
    ('Chevy', 'Silverado'): [2018, 2024],
    ('Kia', 'Forte'): [2023, 2024],
    ('Kia', 'Stinger'): [2022, 2023]
}
'''

config.add_dependency('model', 'make', make_model_mapping)
config.add_dependency('condition', 'year', year_condition_mapping)
config.add_dependency('owners', 'condition', condition_owner_mapping)
#config.add_dependency('year', ('make', 'model'), make_model_year_mapping)

data_generator = DataForge(config)
df = data_generator.generate(10)
print(df)