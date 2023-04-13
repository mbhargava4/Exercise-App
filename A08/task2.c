#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "sumArray.h"

double get_random_number() {
    return (double) rand() / RAND_MAX * 2 - 1;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s n\n", argv[0]);
        return 1;
    }

    const size_t n = atoi(argv[1]);

    double* A = (double*) malloc(n * n * sizeof(double));
    if (A == NULL) {
        printf("Failed to allocate memory for matrix A\n");
        return 1;
    }

    srand(time(NULL));
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            A[i * n + j] = get_random_number();
        }
    }

    clock_t start_time = clock();
    double sum1 = sumArray1(A, n);
    clock_t end_time = clock();
    double time1 = (double) (end_time - start_time) * 1000 / CLOCKS_PER_SEC;

    start_time = clock();
    double sum2 = sumArray2(A, n);
    end_time = clock();
    double time2 = (double) (end_time - start_time) * 1000 / CLOCKS_PER_SEC;

    printf("sumArray1:\t%lf\t%lf\n", sum1, time1);
    printf("sumArray2:\t%lf\t%lf\n", sum2, time2);

    free(A);
    return 0;
}