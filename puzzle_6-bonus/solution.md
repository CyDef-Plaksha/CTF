# Solution to "Cydef's Mistake"

To solve this problem, it is necessary to refer to the poster for the event.

The poster has a C Program in a file `errno.c` (provided here) which is the following:

```c
#include <stdio.h>
#include <math.h>
#include <errno.h>
#include <stdlib.h>

#define N 10
#define NEG(X) (-(X))

int main() {
    double a;
    a = log(NEG(N));
}
```

(file: `errno.c`)

As per the poster, the above file is compiled using the command `gcc errno.c -lm` and run by `./a.out`.

Trying the commands above, we don't get any errors and the program executes. However, there is a *fatal* error that's seen by the *computer*. This can be checked using the `errno.h` library (the file name was a hint!).

The way to check this (from a quick Google search), is the following:

```c
#include <stdio.h>
#include <math.h>
#include <errno.h>
#include <stdlib.h>F

#define N 10
#define NEG(X) (-(X))

int main() {
    double a;
    errno = 0;
    a = log(NEG(N));
    if (errno != 0) {
        printf("Error occured: %d!\n", errno);
    }
}
```

(file: `errno_edited.c`)

The error code seen by the computer is a Division/0, and it's flag is `33`.

FLAG: **`33`**