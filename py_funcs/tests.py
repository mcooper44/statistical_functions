import unittest
import random
import central
import s_math
import digital
import statistics as stats



class Test_bin_to_hex(unittest.TestCase):

    def test_random_bin(self):
        test_set = [bin(random.randint(0, 1000)) for _ in range(0,10)]
        for t in test_set:
            h_value = f'0x{int(t[2:],2):X}'
            self.assertTrue(h_value.__eq__(digital.bin_to_hex(t, True)))


class Test_int_to_hex(unittest.TestCase):

    def test_ints(self):
        test_rack = [(1,'1'),(5, '5'), (10,'A'), (15, 'F'),
                     (300, '12C'), (500, '1F4'), (1000000,'F4240')]
        for n, s in test_rack:
            self.assertTrue(digital.int_to_hex(n).__eq__(s))


class Test_bin_int(unittest.TestCase):

    def test_simple_int(self):
        bin_str = '110101'
        self.assertTrue(int(bin_str, 2).__eq__(digital.bin_to_int(bin_str)))


class Test_int_to_bin(unittest.TestCase):
    def test_simple_bin(self):
        self.assertTrue(bin(2).__eq__(digital.int_to_bin(2, True)))


class Test_product(unittest.TestCase):
    def test_list_int(self):
        idata = [1, 2, 3]
        result = s_math._product(idata)
        self.assertEqual(result, 6)

    def test_list_float(self):
        fdata = [2.5, 3.75, 6.0]
        self.assertEqual(s_math._product(fdata), 56.25)

    def test_bad_str(self):
        with self.assertRaises(TypeError):
            s_math._product('Hello Friend')


class Test_sum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        self.assertEqual(s_math._sum(data), 6)

    def test_list_float(self):
        self.assertEqual(s_math._sum([1.0, 2.0, 3.0]), 6.0)

    def test_bad_str(self):
        with self.assertRaises(TypeError):
            s_math._sum('Hello Friend')


class Test_sqrt(unittest.TestCase):
    def test_int(self):
        self.assertEqual(s_math._sqrt(100), 10.0)

    def test_float(self):
        self.assertEqual(s_math._sqrt(100.0), 10.0)

    def test_float_complex(self):
        self.assertEqual(s_math._sqrt(5.2), 2.280350850198276)

    def test_zero_value(self):
        self.assertEqual(s_math._sqrt(0), 0.0)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            s_math._sqrt(-1)


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
