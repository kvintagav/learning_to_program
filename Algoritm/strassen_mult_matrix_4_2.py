"""
	Прогшрамма для алгоритма Штрассена умножения матриц
"""
from random import randrange
import sys

DISCHARGE = 8
MODULE = 5

def full_matrix():
	Matrix = []
	for index in range(DISCHARGE):
		String = []
		for j_ind in range(DISCHARGE):
			String.append(randrange(MODULE))
		Matrix.append(String)
			
	return Matrix		

def print_matrix(Matrix):
	for string in Matrix:
		print (string)

def multiply_matrix(A_matr , B_matr):
	"""Сложность алгоритма О(n^3) """
	rez_matrix= []
	for string in range(DISCHARGE):
		row_matrix=[]
		for row  in range(DISCHARGE):
			cell = 0
			for k in range(DISCHARGE):
				cell+=A_matr[string][k]*B_matr[k][row]
			row_matrix.append(cell)
		rez_matrix.append(row_matrix)

	return rez_matrix

def razbienie_matrix(matrix,number):
	rez_matrix = []
	

	return rez_matrix

def smultiply_matrix_recursive(A_matr, B_Matr):
	C_matrix = []

	
	return C_matrix

def smultiply_matrix_strassen(A_matr, B_Matr):
	C_matrix = []

	center 
	return C_matrix


Matrix_A = full_matrix()
Matrix_B = full_matrix()

Matrix_C = multiply_matrix(Matrix_A,Matrix_B)

print ("Matrix_A:")
print_matrix(Matrix_A)
print ("Matrix_B:")
print_matrix(Matrix_B)
print ("Matrix_C:")
print_matrix(Matrix_C)
