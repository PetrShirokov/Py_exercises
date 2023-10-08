from operator import add
from functools import reduce


def transposed(matr):
    matrix = matr[:]
    t_matrix = [[]] * len(matrix[0])
    for i in range(0, len(matrix[0])):
        new_line = []
        for j in range(0, len(matrix)):
            new_line.append(matrix[j][i])
        t_matrix[i] = new_line
    return t_matrix


def calc_matrix_element(list1, list2):
    res_list = []
    for tup in list(zip(list1, list2)):
        res_list.append(tup[0] * tup[1])
    return reduce(add, res_list)


def multiply(A, B):
    C = [[]] * len(A)
    B_trans = transposed(B)
    for line in range(len(A)):
        current_line = []
        for i in range(len(B_trans)):
            list1 = A[line]
            list2 = B_trans[i]
            current_element = calc_matrix_element(list1, list2)
            current_line.append(current_element)
            C[line] = current_line
    return C


A = [[2, 5], [6, 7], [1, 8]]
B = [[1, 2, 1], [0, 1, 0]]
# multiply(A,B) -> [[2, 9, 2], [6, 19, 6], [1, 10, 1]]
print(multiply(A, B))
