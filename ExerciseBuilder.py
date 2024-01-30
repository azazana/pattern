class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = {}

    def add_field(self, type, name):
        self.fields[type] = name
        return self

    def __str__(self):
        lines = []
        lines.append(f'class {self.root_name}:')
        lines.append(f'    def __init__(self):')
        for key, value in self.fields.items():
            lines.append(f"        self.{key}={value}")
        return '\n'.join(lines)


cb = CodeBuilder('Person').add_field('name', '""') \
    .add_field('age', '0')
print(cb)
