from population import Population
class IO_helper:
    @staticmethod
    def stringify(data : list[Population]):
        return '\n'.join(f"{pop.country},{pop.year},{pop.population}" for pop in data)

    @staticmethod
    def save(path, data : list[Population]):
        with open(path, 'w') as f:
            f.write(IO_helper.stringify(data))