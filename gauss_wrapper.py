from ctypes import CDLL, c_int, c_double, Structure, POINTER
import os
import numpy as np 


class Matrix(Structure):
    _fields_ = [
        ("rows", c_int),
        ("cols", c_int),
        ("data", POINTER(c_double)),
        ("rank", c_int)
    ]

def get_ready():
    """reads .so file"""


    current_dir = os.path.dirname(os.path.abspath(__file__))
    lib_path = os.path.join(current_dir, 'gauss_elimination.so')
    lib = CDLL(lib_path) # read .so / .dll

    # passing arguments
    lib.gaussian_elimination.argtypes = [c_int, c_int, POINTER(c_double)] 
    lib.gaussian_elimination.restype = POINTER(Matrix)
    lib.get_rank.argtypes = [POINTER(Matrix)]
    lib.get_rank.restype = c_int


    return lib


def get_matrix_rank(matrix, dim) -> float:
    lib = get_ready() # call CDLL

    rows, cols = dim
    c_arr = (c_double * len(matrix.flatten()))(*matrix.flatten()) # C works with flattened arrays
    result_ptr = lib.gaussian_elimination(rows, cols, c_arr) # calling C function
    rank = lib.get_rank(result_ptr) # getting rank
    lib.free_matrix(result_ptr) # free memory
    return rank

