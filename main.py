import pandas as pd
import numpy as np

from gauss_wrapper import get_matrix_rank
from determinant import determinant


if __name__ == "__main__":
    # reading our data
    test_cases = pd.read_json('input.json')
    
    for test_case in test_cases['test_cases']:
        dim = test_case['input']['dimensions']
        matrix = test_case['input']['matrix']
        ground_truth = test_case['output']

        det = 0 
        if dim[0] == dim[1]:
            det = determinant(matrix)

        # here we kill two birds with one stone
        if det != 0: # if it's non-singular (full rank), then rank is order of A
            print(f"rank = {dim[0]}, ground truth is {ground_truth}")
        else:
            print(np.array(matrix))

            rank = get_matrix_rank(np.array(matrix), dim)

            print(f"rank = {rank}, ground truth is {ground_truth}")


