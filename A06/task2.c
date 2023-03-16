#include <stdio.h>
#include <stdlib.h>
#include "structs.h"

int main() {
    //Part B
    printf("Size of struct A: %zu bytes\n", sizeof(struct A)); // Print size of struct A
    printf("Size of struct B: %zu bytes\n", sizeof(struct B)); //Print size of struct B

    //Part C
    struct A* a = (struct A*)malloc(sizeof(struct A));

    //Part D
    a->i = 16;
    a->c = 'm';
    a->d = 3.14;

    //Part E
    printf("int i: %d\n", a->i);
    printf("char c: %c\n", a->c);
    printf("double d: %f\n", a->d);

    //Part F
    free(a);

    return 0;
}