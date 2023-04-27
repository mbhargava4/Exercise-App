#include <stdio.h>
#include <math.h>

//code for float commented out
//float g(float x) {
//    return sinf(x) / x;
//}

//int main() {
//    float a = 0.0f, b = 1.0f;
//    while (b - a > 1e-7f) {  // continue until range is small enough
//        float m = (a + b) / 2.0f;
//        if (g(m) >= 1.0f) {
//            b = m;  // search lower half
//        } else {
//            a = m;  // search upper half
//        }
//    }
//    printf("%.10f\n", a);  // print xf
//    return 0;
//}


double g(double x) {
    return sin(x) / x;
}

int main() {
    double a = 0.0, b = 1.0;
    while (b - a > 1e-15) {  // continue until range is small enough
        double m = (a + b) / 2.0;
        if (g(m) >= 1.0) {
            b = m;  // search lower half
        } else {
            a = m;  // search upper half
        }
    }
    printf("%.20f\n", a);  // print xd
    return 0;
}

