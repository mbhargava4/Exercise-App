#include "matmul.h"

// mmul1: C = A B, where A, B, and C are n x n matrices stored in row-major order
void mmul1(const double* A, const double* B, double* C, const size_t n) {
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            double sum = 0.0;
            for (size_t k = 0; k < n; k++) {
                sum += A[i*n+k] * B[k*n+j];
            }
            C[i*n+j] = sum;
        }
    }
}

// mmul2: C = A B, where A, B, and C are n x n matrices stored in row-major order
void mmul2(const double* A, const double* B, double* C, const size_t n) {
    for (size_t j = 0; j < n; j++) {
        for (size_t i = 0; i < n; i++) {
            double sum = 0.0;
            for (size_t k = 0; k < n; k++) {
                sum += A[i*n+k] * B[k*n+j];
            }
            C[i*n+j] = sum;
        }
    }
}

// mmul3: C = A B, where A and C are n x n matrices stored in row-major order, and B is n x n
// matrix stored in column-major order
void mmul3(const double* A, const double* B, double* C, const size_t n) {
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            double sum = 0.0;
            for (size_t k = 0; k < n; k++) {
                sum += A[i*n+k] * B[j*n+k];
            }
            C[i*n+j] = sum;
        }
    }
}

// mmul4: C = A B, where A and B are n x n matrices stored in column-major order, and C is an
// n x n matrix stored in row-major order
void mmul4(const double* A, const double* B, double* C, const size_t n) {
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            double sum = 0.0;
            for (size_t k = 0; k < n; k++) {
                sum += A[k*n+i] * B[k*n+j];
            }
            C[i*n+j] = sum;
        }
    }
}