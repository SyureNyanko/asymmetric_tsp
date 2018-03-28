# -*- coding: utf-8 -*-


from context import asymmetric_tsp 
import unittest

import math

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def get_standardfunc(self):
    	def func(v1, v2):
    		'''Measure length or cost'''
    		dv = (v1[0] - v2[0], v1[1] - v2[1])
    		d2 = dv[0] * dv[0] + dv[1] * dv[1]
    		d = math.sqrt(d2)
    		return d
    	return func
    def test_two_opt(self):
    	expected = [[0, 0], [1, 2], [4, 5], [10, 0], [2, 0]]
    	point_table = [[0,0],[1,2],[10,0],[4,5],[2,0]]
    	actual = asymmetric_tsp.core.two_opt(point_table, self.get_standardfunc())
    	self.assertEqual(expected, actual)

    def test_timeout(self):
    	expected = [[0, 0], [1, 2], [4, 5], [10, 0], [2, 0]]
    	point_table = [[0,0],[1,2],[10,0],[4,5],[2,0]]
    	with self.assertRaises(TimeoutError):
    		asymmetric_tsp.core.two_opt(point_table, self.get_standardfunc(), limittime=0)

if __name__ == '__main__':
	unittest.main()