#include<stdio.h>
#include<gsl/gsl_ieee_utils.h>

int main() {
    float f = 1.0;
    for(int i = 0; i<=150; i++) {
        gsl_ieee_printf_float(&f);
        printf("\n");
        f /= 2.0;
    }

    return 0;
}