#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "matmul.c"


int main()
{
   const size_t n = 1024;
    double *A = malloc(n * n * sizeof(double));
    double *B = malloc(n * n * sizeof(double));
    double *C1 = malloc(n * n * sizeof(double));
    double *C2 = malloc(n * n * sizeof(double));
    double *C3 = malloc(n * n * sizeof(double));
    double *C4 = malloc(n * n * sizeof(double));

    srand(time(NULL));
    for (size_t i = 0; i < n * n; i++) {
        A[i] = (double)rand() / (double)RAND_MAX * 2.0 - 1.0;
        B[i] = (double)rand() / (double)RAND_MAX * 2.0 - 1.0;
    }

    clock_t start_time = clock();
    mmul1(A, B, C1, n);
    clock_t end_time = clock();
    double elapsed_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
    printf("t1\n%f\n", elapsed_time);

    clock_t start_time_2 = clock();
    mmul2(A, B, C2, n);
    clock_t end_time_2 = clock();
    double elapsed_time_2 = (double)(end_time_2 - start_time_2) / CLOCKS_PER_SEC;
    printf("t2\n%f\n", elapsed_time_2);

    clock_t start_time_3 = clock();
    mmul3(A, B, C3, n);
    clock_t end_time_3 = clock();
    double elapsed_time_3 = (double)(end_time_3 - start_time_3) / CLOCKS_PER_SEC;
    printf("t3\n%f\n", elapsed_time_3);

    clock_t start_time_4 = clock();
    mmul4(A, B, C4, n);
    clock_t end_time_4 = clock();
    double elapsed_time_4 = (double)(end_time_4 - start_time_4) / CLOCKS_PER_SEC;
    printf("t4\n%f\n", elapsed_time_4);

    free(A);
    free(B);
    free(C1);
    free(C2);
    free(C3);
    free(C4);
    return 0;
}