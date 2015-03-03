"""
	Прогшрамма для алгоритма Штрассена умножения матриц
"""
from random import randomint
import sys

DISCHARGE = 5
MODULE = 10

def full_matrix():
	Matrix = []
	for index in range(DISCHARGE):
		String = []
		for j_ind in range(DISCHARGE):
			String.append(randomint(MODULE))
		Matrix.append(String)
			
	return Matrix		

def print_matrix(Matrix):
	for string in Matrix:
	print 