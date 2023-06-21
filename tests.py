import unittest
from py_funcs import central


class Test_product(unittest.TestCase):
    def test_list_int(self):
        idata = [1, 2, 3]
        result = central._product(idata)
        self.assertEqual(result, 6)

    def test_list_float(self):
        fdata = [2.5, 3.75, 6.0]
        self.assertEqual(central._product(fdata), 56.25)

    def test_bad_str(self):
        with self.assertRaises(TypeError):
            central._product('Hello Friend')


class Test_sum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        self.assertEqual(central._sum(data), 6)


class Test_sqrt(unittest.TestCase):
    def test_int(self):
        self.assertEqual(central._sqrt(100), 10.0)

    def test_float(self):
        self.assertEqual(central._sqrt(100.0), 10.0)

    def test_float_complex(self):
        self.assertEqual(central._sqrt(5.2), 2.280350850198276)


class Test_geometric_mean(unittest.TestCase):
    def test_list_int(self):
        x = 5.210342169394704
        self.assertEqual(central.geometric_mean([2, 4, 6, 8, 10]), x)


if __name__ == '__main__':
    unittest.main()
