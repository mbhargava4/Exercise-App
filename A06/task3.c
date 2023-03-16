#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // check that there is exactly one command line argument
    if (argc != 2) {
        if(argc==1){
            printf("No argument enetered");
        }else{
            printf("More than 2 arguments entered");
        }
        return 0;
    }

    // convert the command line argument to an integer
    int N = atoi(argv[1]);

    // check that the integer is positive
    if (N <= 0) {
        printf("Argument entered is not a positive integer greater than 0");
        return 0;
    }

    int* a = (int*) malloc((N + 1) * sizeof(int));
    for (int i = 0; i < N+1; i++) {
        a[i] = i;
    }

    for (int i = 0; i <= N; i++) {
        printf("%d ", a[i]);
    }
     printf("\n");

    // sort the array in descending order using qsort
    qsort(a, N + 1, sizeof(int), compare);

    // print the sorted array
    for (int i = 0; i <= N; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    free(a);

    return 0;
}

// helper function for qsort 
int compare(const void* a, const void* b) {
    int A = *((int*) a);
    int B = *((int*) b);
    return B - A;
}