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

    def test_list_float(self):
        self.assertEqual(central._sum([1.0, 2.0, 3.0]), 6.0)

    def test_bad_str(self):
        with self.assertRaises(TypeError):
            central._sum('Hello Friend')


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


class Test_mean(unittest.TestCase):
    '''
    test sample population and weighted mean
    '''
    def test_sample_mean_list_int(self):
        self.assertEqual(central.sample_mean([1, 3, 9, 81]), 23.5)

    def test_population_mean_list_int(self):
        self.assertEqual(central.population_mean([1, 3, 9, 81]), 23.5)

    def test_weighted_mean_list_int(self):
        x = 15.28571429
        self.assertEqual(round(
            central.weighted_mean([1, 1, 3, 3, 9, 9, 81]), 8), x)


class Test_statistical_range(unittest.TestCase):
    pass


class Test_MAD(unittest.TestCase):
    pass


class Test_variance(unittest.TestCase):
    pass


class Test_standard_deviation(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
