'''
Двумерные массивы.
Поиск элемента A[i, j] == A[i * M + j] - линеаризация массива.
N строк, M элементов в строке 
ЭТО ПЕРВЫЙ ПУТЬ

ВТОРОЙ ПУТЬ:
список списков:
А = [[0]*M]*N - ТАК СОЗДАВАТЬ ДВУМЕРНЫЙ МАССИВ НЕЛЬЗЯ!!!

A = [[0]*M for i in range(N)] - ВОТ ТАК НУЖНО СОЗДАВАТЬ МАССИВ
ПОЛУЧИМ:
A = [
	[0, 0 , 0],  - A[0]
	[0, 0 , 0],  - A[1]
	[0, 0 , 0],  - A[2]
	[0, 0 , 0],  - A[3]
]
A[0] == A[1]
НО!!!
A[0] is A[1]  -- False (это не одно и тоже)
'''