#include "math_utils.h"
#include <math.h>

float Sum(const float* arr, size_t count) {
    float sum = 0.0;
    for (size_t i = 0; i < count; i++) {
        sum += arr[i];
    }
    return sum;
}

float SumSines(const float* arr, size_t count) {
    float sum_sines = 0.0;
    for (size_t i = 0; i < count; i++) {
        sum_sines += sin(arr[i]);
    }
    return sum_sines;
}

void Fusion(const float* arr, size_t count, float* sum, float* sum_sines) {
    *sum = 0.0;
    *sum_sines = 0.0;
    for (size_t i = 0; i < count; i++) {
        *sum += arr[i];
        *sum_sines += sin(arr[i]);
    }
}
