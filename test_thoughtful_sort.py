import unittest
from thoughtful_sort import sort

class TestThoughtfulSort(unittest.TestCase):
    def test_standard_small_light(self):
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")

    def test_heavy_only(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_bulky_by_volume_only(self):
        # 100*100*100 = 1_000_000 -> bulky
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")

    def test_bulky_by_dimension_only(self):
        self.assertEqual(sort(150, 1, 1, 1), "SPECIAL")

    def test_both_bulky_and_heavy(self):
        self.assertEqual(sort(150, 1, 1, 20), "REJECTED")

    def test_edge_equalities(self):
        # Exactly at thresholds should trigger
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")  # bulky by volume and heavy
        # Strictly below all thresholds: dims <150, volume <1_000_000, mass <20
        self.assertEqual(sort(149.9, 149.9, 20, 19.999), "STANDARD")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 1)
        with self.assertRaises(ValueError):
            sort(10, -1, 10, 1)
        with self.assertRaises(ValueError):
            sort(10, 10, -1, 1)
        with self.assertRaises(ValueError):
            sort(10, 10, 10, -0.1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
