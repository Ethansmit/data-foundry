import numpy as np
import pandas as pd

from .config import Config

class DataForge:
    def __init__(self, config: Config):
        self.config = config
    
    def generate(self, n):
        data = {}
        
        for name, values in self.config.get_schema().items():
                data[name] = np.random.choice(values,n)
            
        df = pd.DataFrame(data)
        return df