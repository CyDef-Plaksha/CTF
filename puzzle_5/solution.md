# Solution to "The harmony behind servers"

This problem is a "code golf" problem. This means that it is a problem of trying to write an algorithm in the *least* amount of characters.

In our case, the program must do the following task:

Convert a 2D array (key) into a matrix of 0's and 1's, where 0's are in the odd indexes and 1's are in the even indexes.

The 2D Array is given in the form:

```sh
4 5 6 3 4 9 3 4|3 4 5 6 4 5 6 8| ...
```

To solve this problem, we must write a code that achieves the above in less than **52 characters**. We can see that the limit is 52 characters by analysing `golf.py`. The program can also be tested using `golf.py`.

There can be multiple solutions to this problem. The solution to the problem is the flag.

One of the solutions is the following:

FLAG: **`[[int(e)%2 for e in r[::2]] for r in x.split("|")]`**
