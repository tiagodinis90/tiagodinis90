import unittest
from pathlib import Path
from reproduce import stats,reproduce,svg
DATA=Path(__file__).resolve().parents[1]/'data/anscombe.csv'
class ReproTests(unittest.TestCase):
    def test_count(self):
        data,out=reproduce(DATA)
        self.assertEqual(len(out),4)
        self.assertTrue(all(a['n']==11 for a in out.values()))
    def test_regression_reference(self):
        _,out=reproduce(DATA)
        for s in out.values():
            self.assertAlmostEqual(s['mean_x'],9.0,places=6)
            self.assertAlmostEqual(s['mean_y'],7.5,delta=.01)
            self.assertAlmostEqual(s['slope'],.5,delta=.005)
            self.assertAlmostEqual(s['intercept'],3,delta=.03)
            self.assertAlmostEqual(s['r_squared'],.666,delta=.005)
    def test_different_x_distribution(self):
        data,_=reproduce(DATA);self.assertEqual(data['4'][0].count(8),10)
        self.assertNotEqual(data['1'][0],data['4'][0])
    def test_svg_has_points(self):
        data,out=reproduce(DATA);self.assertEqual(svg(data,out).count('<circle'),44)
    def test_invalid_zero_variance(self):
        with self.assertRaises(ValueError):stats([1,1,1],[2,3,4])
    def test_invalid_nan(self):
        with self.assertRaises(ValueError):stats([1,2,float('nan')],[2,3,4])
