import unittest

import kal


class AritmetikaTest(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(kal.tambah(2, 3), 5)
        self.assertEqual(kal.tambah(-2, 3), 1)
        self.assertEqual(kal.tambah(2.5, 0.5), 3.0)

    def test_kurang(self):
        self.assertEqual(kal.kurang(10, 4), 6)
        self.assertEqual(kal.kurang(4, 10), -6)

    def test_kali(self):
        self.assertEqual(kal.kali(6, 7), 42)
        self.assertEqual(kal.kali(-3, 3), -9)
        self.assertEqual(kal.kali(0, 100), 0)

    def test_bagi(self):
        self.assertEqual(kal.bagi(9, 3), 3)
        self.assertEqual(kal.bagi(1, 4), 0.25)
        self.assertIn("pembagian dengan nol", kal.bagi(5, 0))

    def test_pangkat(self):
        self.assertEqual(kal.pangkat(2, 10), 1024)
        self.assertEqual(kal.pangkat(9, 0.5), 3.0)

    def test_modulo(self):
        self.assertEqual(kal.modulo(10, 3), 1)
        self.assertEqual(kal.modulo(-7, 2), 1)
        self.assertIn("modulo dengan nol", kal.modulo(5, 0))

    def test_rata_rata(self):
        self.assertEqual(kal.rata_rata(2, 4, 6), 4)
        self.assertEqual(kal.rata_rata(10), 10)
        self.assertIn("minimal satu angka", kal.rata_rata())


if __name__ == "__main__":
    unittest.main()
