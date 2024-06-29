class Config:
    def __init__(self):
        self.schema = {}
        
    def add_attribute(self, name, values):
        if name in self.schema:
            raise ValueError(f"Attribute '{name}' already exists in the schema.")
        self.schema[name] = values
    
    def remove_attribute(self, name):
        if name not in self.schema:
            raise ValueError(f"Attribute '{name}' does not exist in the schema.")
        del self.schema[name]
    
    def get_schema(self):
        return self.schema
    
    def set_schema(self, schema):
        self.schema = schema