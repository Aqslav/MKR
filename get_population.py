from IO_helper import IO_helper
from population import Population

class PopulationDataManager:
    @staticmethod
    def sort_by_population(data : list[Population]):
        return sorted(data, key=lambda x: x.population)