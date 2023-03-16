#include <stdio.h>
#include <stdlib.h>
#include "structs.h"

int main() {
    // Print size of struct A
    printf("Size of struct A: %zu bytes\n", sizeof(struct A));
    printf("Size of struct B: %zu bytes\n", sizeof(struct B));
    return 0;
}