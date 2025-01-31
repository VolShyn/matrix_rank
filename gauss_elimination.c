#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

typedef struct {
    int rows;
    int cols;
    double* data;
    int rank;
} Matrix;

Matrix* gaussian_elimination(int rows, int cols, double* input_matrix) {
    Matrix* result = (Matrix*)malloc(sizeof(Matrix));
    result->rows = rows;
    result->cols = cols;
    result->rank = 0;
    
    const double EPSILON = 1e-10;
    
    size_t size = rows * cols * sizeof(double);
    result->data = (double*)malloc(size);
    memcpy(result->data, input_matrix, size);

    int rank = 0;
    int lead = 0;

    for (int r = 0, lead = 0; r < rows && lead < cols; ) {
        // find pivot row in the current column
        int pivotRow = r;
        double maxVal = fabs(result->data[r * cols + lead]);
        for (int i = r + 1; i < rows; i++) {
            double val = fabs(result->data[i * cols + lead]);
            if (val > maxVal) {
                maxVal = val;
                pivotRow = i;
            }
        }

        // If no nonzero pivot in this column, skip the column
        if (maxVal < EPSILON) {
            lead++;
            continue;
        }

        // swapping to put pivot in row r if needed
        if (pivotRow != r) {
            for (int j = 0; j < cols; j++) {
                double temp = result->data[r * cols + j];
                result->data[r * cols + j] = result->data[pivotRow * cols + j];
                result->data[pivotRow * cols + j] = temp;
            }
        }

        // normalizing pivot row
        double pivot = result->data[r * cols + lead];
        for (int j = 0; j < cols; j++) {
            result->data[r * cols + j] /= pivot;
        }

        // eliminate below and above
        for (int i = 0; i < rows; i++) {
            if (i != r) {
                double factor = result->data[i * cols + lead];
                for (int j = 0; j < cols; j++) {
                    result->data[i * cols + j] -= factor * result->data[r * cols + j];
                }
            }
        }

        // moving to the next row and column
        r++;
        lead++;
        rank++;
    }
    
    result->rank = rank;
    return result;
}

void free_matrix(Matrix* matrix) {
    if (matrix) {
        free(matrix->data);
        free(matrix);
    }
}

int get_rank(Matrix* matrix) {
    return matrix->rank;
}