#include <stdio.h>
#include <math.h>
#include <errno.h>
#include <stdlib.h>

#define N 10
#define NEG(X) (-(X))

int main() {
    double a;
    errno = 0;
    a = log(NEG(N));
    printf("Error occured: %d!\n", errno);
}