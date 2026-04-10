from population import Population
class IO_helper:
    @staticmethod
    def stringify(data : list[Population]):
        return '\n'.join(f"{pop.country},{pop.year},{pop.population}" for pop in data)

    @staticmethod
    def save(path, data : list[Population]):
        with open(path, 'w') as f:
            f.write(IO_helper.stringify(data))
    
    @staticmethod
    def load(path):
        with open(path, 'r') as f:
            lines = f.read().split('\n')
            return [IO_helper.parse(line) for line in lines if line]
    
    @staticmethod
    def parse(line):
        country, year, population = line.split(',')
        return Population(country, int(year), int(population))