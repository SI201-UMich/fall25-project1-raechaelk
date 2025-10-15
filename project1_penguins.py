import csv


def read_penguin_data(file):
    with open(file) as inFile:
        lines = inFile.readlines()
    year_d = {}
    lines = lines[1:]
    for line in lines:
        values = line.rstrip().split(',')
        try:
            species = values[1].strip('"') 
            island = values[2].strip('"')
            bill_length = values[3]
            bill_depth = values[4]
            flipper = float(values[5])
            body_mass = float(values[6])
            sex = values[7].strip('"')
            year = int(values[8])
          
            values_d = {}
            values_d["species"] = species
            values_d["flipper_length_mm"] = flipper
            values_d["body_mass_g"] = body_mass
            
            if year not in year_d:
                year_d[year] = []
            year_d[year].append(values_d)
            
        except (ValueError, IndexError) as e:
            continue
    
    return year_d


def calculate_avg_flipper_by_year(data):
    avg_flipper = {}

    for year, penguins in data.items():
        total = 0
        count = 0
        for p in penguins:
            total += p["flipper_length_mm"]
            count += 1
        avg_flipper[year] = round(total / count, 2)

    return avg_flipper

def calculate_avg_body_mass_by_year(data):
    avg_mass = {}

    for year, penguins in data.items():
        total = 0
        count = 0
        for p in penguins:
            total += p["body_mass_g"]
            count += 1
        avg_mass[year] = round(total / count, 2)

    return avg_mass


def write_results_to_csv(results_flipper, results_mass):
    with open("penguin_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Year", "Avg Flipper Length (mm)", "Avg Body Mass (g)"])
        for year in sorted(results_flipper.keys()):
            writer.writerow([
                year,
                results_flipper[year],
                results_mass.get(year, "N/A")
            ])
    print("Results written to penguin_results.csv")


def main():
    data = read_penguin_data("penguins.csv")
    results_flipper = calculate_avg_flipper_by_year(data)
    results_mass = calculate_avg_body_mass_by_year(data)
    write_results_to_csv(results_flipper, results_mass)

    print("Average Flipper Length per Year:", results_flipper)
    print("Average Body Mass per Year:", results_mass)

if __name__ == "__main__":
    main() 