import numpy as np
from typing import Union, List


def get_minor_matrix(matrix: np.ndarray, 
                     col_index: int) -> np.ndarray:
    """reurns a matrix with first row and specified column removed"""
    # removing first row and specified column
    return matrix[1:, np.arange(matrix.shape[1]) != col_index]

def determinant(matrix: Union[List[List[float]], 
                              np.ndarray]) -> float:
    """calculates the determinant of a square matrix using recursive minor expansion"""
    matrix = np.array(matrix)
    
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("provide square matrix")
    
    n = matrix.shape[0]
    
    # base cases
    if n == 1:
        return float(matrix[0, 0])
    if n == 2:
        return float(matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0])
    
    # recursive expansion along the first row
    det = 0.0
    for i in range(n):
        cofactor = (-1) ** i * matrix[0, i]
        minor_det = determinant(get_minor_matrix(matrix, i))
        det += cofactor * minor_det
        
    return det