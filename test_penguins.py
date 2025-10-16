import unittest
import os
import csv
from project1_penguins import (
    read_penguin_data,
    calculate_avg_flipper_by_year,
    calculate_avg_body_mass_by_year,
)


            

class TestPenguinFunctions(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            2007: [
                {"species": "Adelie", "island": "Torgersen", "flipper_length_mm": 180.0, "body_mass_g": 3700.0},
                {"species": "Gentoo", "island": "Dream", "flipper_length_mm": 200.0, "body_mass_g": 4100.0},
                {"species": "Adelie", "island": "Biscoe", "flipper_length_mm": 190.0, "body_mass_g": 3800.0},
            ],
            2008: [
                {"species": "Gentoo", "island": "Dream", "flipper_length_mm": 210.0, "body_mass_g": 4200.0},
                {"species": "Adelie", "island": "Dream", "flipper_length_mm": 195.0, "body_mass_g": 3850.0},
                {"species": "Chinstrap", "island": "Dream", "flipper_length_mm": 205.0, "body_mass_g": 4000.0},
            ],
        }

    def test_read_penguin_data_type(self):
        result = read_penguin_data("penguins.csv")
        self.assertIsInstance(result, dict)

    def test_read_penguin_data_years(self):
        result = read_penguin_data("penguins.csv")
        for year in result.keys():
            self.assertIsInstance(year, int)

    def test_read_penguin_data_contents(self):
        result = read_penguin_data("penguins.csv")
        for year, penguins in result.items():
            self.assertIsInstance(penguins, list)
            if penguins:
                self.assertIsInstance(penguins[0], dict)

    def test_read_penguin_data_has_required_keys(self):
        result = read_penguin_data("penguins.csv")
        for year, penguins in result.items():
            for p in penguins:
                self.assertTrue("species" in p)
                self.assertTrue("island" in p)
                self.assertTrue("flipper_length_mm" in p)
                self.assertTrue("body_mass_g" in p)


    def test_avg_flipper_basic(self):
        result = calculate_avg_flipper_by_year(self.sample_data)
        self.assertEqual(result[2007], 185.0)
        self.assertEqual(result[2008], 195.0)

    def test_avg_flipper_is_dict(self):
        result = calculate_avg_flipper_by_year(self.sample_data)
        self.assertIsInstance(result, dict)

    def test_avg_flipper_edge_empty(self):
        result = calculate_avg_flipper_by_year({})
        self.assertEqual(result, {})

    def test_avg_flipper_single_entry(self):
        result = calculate_avg_flipper_by_year({
            2009: [{"species": "Adelie", "island": "Dream", "flipper_length_mm": 188.0, "body_mass_g": 3600.0}]
        })
        self.assertEqual(result[2009], 188.0)

    def test_avg_body_mass_basic(self):
        result = calculate_avg_body_mass_by_year(self.sample_data)
        self.assertEqual(result[2007], 4100.0)
        self.assertAlmostEqual(result[2008], 4016.67, places=2)

    def test_avg_body_mass_is_dict(self):
        result = calculate_avg_body_mass_by_year(self.sample_data)
        self.assertIsInstance(result, dict)

    def test_avg_body_mass_edge_empty(self):
        result = calculate_avg_body_mass_by_year({})
        self.assertEqual(result, {})

    def test_avg_body_mass_single_entry(self):
        result = calculate_avg_body_mass_by_year({
            2009: [{"species": "Chinstrap", "island": "Dream", "flipper_length_mm": 200.0, "body_mass_g": 4000.0}]
        })
        self.assertEqual(result[2009], 4000.0)


if __name__ == "__main__":
    unittest.main()