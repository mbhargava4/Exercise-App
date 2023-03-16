#include <stdio.h>
#include <stdlib.h>
#include "structs.h"

int main() {
    //Part A
    printf("Size of struct A: %zu bytes\n", sizeof(struct A)); // Print size of struct A
    printf("Size of struct B: %zu bytes\n", sizeof(struct B)); //Print size of struct B

    //Part B
    //Part C
    //Part D
    //Part E
    //Part F

    struct A* a = (struct A*)malloc(sizeof(struct A));
    a->i = 10;
    a->c = 'a';
    a->d = 3.14;

    printf("Field 1: %d\n", a->i);
    printf("Field 2: %c\n", a->c);
    printf("Field 3: %f\n", a->d);

    free(a);


    return 0;
}