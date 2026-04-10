from IO_helper import IO_helper
from population import Population
from get_population import PopulationDataManager
import os


this_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(this_folder)

if __name__ == "__main__":
    data = IO_helper.load('population_data.txt')
    differences = PopulationDataManager.get_difference(data)
    for diff in differences:
        print(IO_helper.stringify([diff]))
    IO_helper.save('population_differences.txt', differences)
    