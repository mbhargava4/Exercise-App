#include <stdio.h>
#include <limits.h>

int main() {
    int a;
    
    // Step 1
    a = INT_MAX;
    printf("Step 1: a = %d\n", a);
    
    // Step 2
    a++;
    printf("Step 2: a = %d\n", a);
    
    // Step 3
    a = INT_MIN;
    printf("Step 3: a = %d\n", a);
    
    // Step 4
    a--;
    printf("Step 4: a = %d\n", a);
    
    return 0;
}
