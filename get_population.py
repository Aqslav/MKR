from IO_helper import IO_helper
from population import Population

class PopulationDataManager:
    @staticmethod
    def sort_by_population(data : list[Population]):
        return sorted(data, key=lambda x: x.population)
    
    @staticmethod
    def get_difference(data : list[Population], country = None):
        if not data:
            return None
        sorted_data = PopulationDataManager.sort_by_population(data)
        differences = []
        for i in range(len(sorted_data)-1):
            if country and sorted_data[i].country != country:
                continue
            diff = sorted_data[i+1].population - sorted_data[i].population
            differences.append(Population(sorted_data[i].country, sorted_data[i].year, diff))
        return differences