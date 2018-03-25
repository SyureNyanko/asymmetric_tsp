# -*- coding: utf-8 -*-
import math
import time
import sys

def testlength(v1, v2):
	'''Measure length or cost'''
	#t = (x1 - x2) * 100
	#return t
	#print(str(v1) + " , " + str(v2))
	dv = (v1[0] - v2[0], v1[1] - v2[1])
	d2 = dv[0] * dv[0] + dv[1] * dv[1]
	d = math.sqrt(d2)
	return d

def route_swap(s, a, b):
	'''Generate new route s is old route, a and b are indexes'''
	new_route = s[0:a+1]
	mid = s[a+1:b+1]
	new_route = new_route + mid[::-1]
	new_route = new_route + s[b+1:]
	return new_route


def calc_route_length(route, f):
	ret = 0
	for i in range(len(route)):
		ret += f(route[i], route[(i+1)%len(route)])
	return ret


def two_opt(route, length_function):
	'''Peforms 2-opt search to improve route'''
	bestroute = route
	l = len(bestroute)
	bestroute_cost = calc_route_length(bestroute, length_function)

	while(True):
		flag = True
		for i in range(l-2):
			i_next = (i + 1)%l
			for j in range(i + 2, l):
				j_next = (j + 1)%l
				if i == 0 and j_next == 0:
					continue
				swapped_route = route_swap(bestroute, i, j)
				swapped_route_cost = calc_route_length(swapped_route, length_function)
				if swapped_route_cost < bestroute_cost:
					print(str(i) + "," + str(j) + "," + str(bestroute))
					bestroute_cost = swapped_route_cost
					bestroute = swapped_route
					flag = False

		if flag:
			break

	return bestroute



def main(points, length_function):
    """Contemplation..."""
    return two_opt(points, length_function)


if __name__ == '__main__':
	'''point_tables is example case'''
	point_table = [(0,0),(1,2),(10,0),(4,5),(2,0)]
	point_size = len(point_table)
	print("initial :" + str(point_table))
	bestroute = main(point_table, testlength)
	print("result  :" + str(bestroute))



