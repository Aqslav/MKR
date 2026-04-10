from population import Population


class PopulationDataManager:
    @staticmethod
    def sort_by_year(data: list[Population]):
        return sorted(data, key=lambda x: x.year)

    @staticmethod
    def get_difference(data: list[Population], country=None):
        if not data:
            return None
        sorted_data = PopulationDataManager.sort_by_year(data)
        sorted_data = [pop for pop in sorted_data 
                       if country is None or pop.country == country]
        differences = []
        for i in range(len(sorted_data)-1):
            diff = sorted_data[i+1].population - sorted_data[i].population
            differences.append(Population(sorted_data[i].country, sorted_data[i].year, diff))
        return differences
