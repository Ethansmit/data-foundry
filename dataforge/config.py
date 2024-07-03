class Config:
    def __init__(self):
        self.schema = {}
        self.dependencies = {}

    def add_attribute(self, name, values):
        if name in self.schema:
            raise ValueError(f"Attribute '{name}' already exists in the schema.")
        self.schema[name] = values

    def add_dependency(self, attribute, dependency, dependency_mapping):
        if attribute not in self.schema or dependency not in self.schema:
            raise ValueError(f"Both '{attribute}' and '{dependency}' must be in the schema to add a dependency.")
        self.dependencies[attribute] = (dependency, dependency_mapping)

    def remove_attribute(self, name):
        if name not in self.schema:
            raise ValueError(f"Attribute '{name}' does not exist in the schema.")
        del self.schema[name]

    def get_schema(self):
        return self.schema

    def get_dependencies(self):
        return self.dependencies

    def set_schema(self, schema):
        self.schema = schema

    def set_dependencies(self, dependencies):
        self.dependencies = dependencies