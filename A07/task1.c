#include "sort.h"

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define ARRAY_SIZE 15

void print_array(const int* A, size_t n)
{
    for (size_t i = 0; i < n; ++i) {
        printf("%d ", A[i]);
    }
    printf("\n");
}

int main(void)
{
    int A[ARRAY_SIZE];

    /* Fill the array with random values */
    srand(time(NULL));
    for (size_t i = 0; i < ARRAY_SIZE; ++i) {
        A[i] = rand() % 100;
    }

    print_array(A, ARRAY_SIZE);

    sort(A, ARRAY_SIZE);

    print_array(A, ARRAY_SIZE);

    return 0;
}






