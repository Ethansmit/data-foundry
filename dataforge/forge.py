import numpy as np
import pandas as pd

from .config import Config

class DataForge:
    def __init__(self, config: Config):
        self.config = config

    def generate(self, n):
        data = {}
        dependencies = self.config.get_dependencies()

        for name, values in self.config.get_schema().items():
            if name in dependencies:
                # Handle dependencies
                dependency, dependency_mapping = dependencies[name]
                dependent_values = data[dependency]
                data[name] = [
                    np.random.choice(dependency_mapping[val])
                    for val in dependent_values
                ]
            else:
                data[name] = np.random.choice(values, n)

        df = pd.DataFrame(data)
        return df