import unittest
from py_funcs import central
import statistics as stats


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
    def test_srange_list(self):
        self.assertEqual(central.statistical_range([10, 20]), 10)


class Test_MAD(unittest.TestCase):
    def test_MAD_list(self):
        data = data = [75, 69, 56, 46, 47, 79, 92, 97, 89, 88,
                       36, 96, 105, 32, 116, 101, 79, 93, 91, 112]
        x = 20.055000000000003
        self.assertEqual(central.mean_absolute_deviation(data), x)


class Test_variance(unittest.TestCase):
    def test_variance_list(self):
        data = [10, 20, 40, 80, 160, 320]
        self.assertEqual(central.variance(data), stats.variance(data))


class Test_standard_deviation(unittest.TestCase):
    def test_stdev_list(self):
        data = [75, 69, 56, 46, 47, 79, 92, 97, 89, 88]
        self.assertEqual(central.standard_deviation(data), stats.stdev(data))


if __name__ == '__main__':
    unittest.main()
