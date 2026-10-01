import json
from pathlib import Path

def save_to_json(data, filename="countries.json"):
    """ Save the list of countries to a JSON file. """
    with Path(filename).open("w") as file:
        json.dump(data, file)
        
    
def read_from_json(filename="countries.json"):
    """ Read the list of countries from a JSON file. """
    with Path.open(filename, "r") as file:
        return json.load(file)

def main():
    countries = []
    print("Enter country names (type 'quit' to finish):")
    
    while True:
        country = input("Country: ")
        if country.lower() == 'quit':
            break
        countries.append(country)
        
        # save the list to a JSON file 
        
        save_to_json(countries)
        
        saved_countries = read_from_json()
        print("\n You've added the following countries:")
        for country in saved_countries:
            print(f" - {country}")
            

if __name__ == "__main__":
    main()