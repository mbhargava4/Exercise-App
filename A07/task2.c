#include "mvmul.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mvmul.h"

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: ./task2 n\n");
        return 1;
    }
    int n = atoi(argv[1]);

    double *A = (double *)malloc(n * n * sizeof(double));
    double *b = (double *)malloc(n * sizeof(double));
    double *c = (double *)malloc(n * sizeof(double));

    srand(time(NULL));
    for (int i = 0; i < n * n; i++) {
        A[i] = ((double)rand() / RAND_MAX) * 2 - 1;
    }

    for (int i = 0; i < n; i++) {
        b[i] = 1.0;
    }

    clock_t start = clock();
    mvmul(A, b, c, n);
    clock_t end = clock();

    printf("%lf\n", c[n-1]);

    free(A);
    free(b);
    free(c);

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC * 1000;
    printf("%lf\n", time_spent);

    return 0;
}