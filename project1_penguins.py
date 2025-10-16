# Name: Rachael Kim
# Student ID: 17003682
# Email: raechael@umich.edu
# Collaborators: Used Claude AI (Anthropic) for debugging CSV issues and test structure

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
            flipper = float(values[5])
            body_mass = float(values[6])
            year = int(values[8])

            values_d = {
                "species": species,
                "island": island,
                "flipper_length_mm": flipper,
                "body_mass_g": body_mass
            }

            if year not in year_d:
                year_d[year] = []
            year_d[year].append(values_d)
        except (ValueError, IndexError):
            continue

    return year_d

def calculate_avg_flipper_by_year(data):
    avg_flipper = {}
    for year, penguins in data.items():
        total = 0
        count = 0
        for p in penguins:
            if p.get("species") == "Adelie" and "flipper_length_mm" in p:
                total += p["flipper_length_mm"]
                count += 1

        if count > 0:
            avg_flipper[year] = float(f"{total / count:.2f}")
    return avg_flipper

def calculate_avg_body_mass_by_year(data):
    avg_mass = {}
    for year, penguins in data.items():
        total = 0
        count = 0
        for p in penguins:
            # Only count penguins from Dream island with valid body mass
            if p.get("island") == "Dream" and "body_mass_g" in p:
                total += p["body_mass_g"]
                count += 1

        if count > 0:
            avg_mass[year] = float(f"{total / count:.2f}")
    return avg_mass


def write_results_to_csv(results_flipper, results_mass):
    with open("penguin_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Year", "Avg Flipper Length (mm)", "Avg Body Mass (g)"])

        all_years = sorted(set(results_flipper.keys()) | set(results_mass.keys()))
        for year in all_years:
            avg_flipper = results_flipper.get(year, "N/A")
            avg_mass = results_mass.get(year, "N/A")

            writer.writerow([year, avg_flipper, avg_mass])

    print("Results written to penguin_results.csv")


def main():
    data = read_penguin_data("penguins.csv")
    results_flipper = calculate_avg_flipper_by_year(data)
    results_mass = calculate_avg_body_mass_by_year(data)
    write_results_to_csv(results_flipper, results_mass)

if __name__ == "__main__":
    main() 