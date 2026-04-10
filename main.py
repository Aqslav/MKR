from IO_helper import IO_helper
from get_population import PopulationDataManager
import os


this_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(this_folder)

if __name__ == "__main__":
    data = IO_helper.load('population_data.txt')
    country = input("Enter a country to filter by (or press Enter to include all): ")
    if country == "":
        country = None
    differences = PopulationDataManager.get_difference(data, country)
    print(IO_helper.stringify(differences))
    IO_helper.save('population_differences.txt', differences)
    input("Press Enter to exit...")
