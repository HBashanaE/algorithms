# Basic Techniques

```markdown
# Inserting Equations for this page

![equation](http://www.sciweavers.org/tex2img.php?eq=ENCODEDEQUATIONHERE&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)
[Encode EQUATION](https://www.url-encode-decode.com)
```

## Mathematics

### Modular Arithmetic

```markdown
(a + b) mod m = (a mod m + b mod m) mod m
(a - b) mod m = (a mod m - b mod m) mod m
(a * b) mod m = (a mod m * b mod m) mod m
```

### Floating Point Numbers

Due to loss of precision, we can't accurately compute floating point numbers. So checking equality in floating point numbers can cause bugs. So use below method to check for equality.

```python
# Two floating point numbers
a = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1+ 0.1
b = 0.1*10
# Precision
epsilon = 1e-9
if abs(a-b)<=epsilon:
    # Equal floating points
    print("Equal")
```

### Sum Formulas

Each sum of the form

![equation](http://www.sciweavers.org/tex2img.php?eq=%5Csum_%7Bx%3D1%7D%5E%7Bn%7D1%5Ek%2B2%5Ek%2B3%5Ek%2B...%2Bn%5Ek&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)

where k is a positive integer, **has a closed-form formula that is a polynomial of degree k +1**. See [Faulhaber’s formula](https://en.wikipedia.org/wiki/Faulhaber%27s_formula).

### Arithmetic Progression

![equation](http://www.sciweavers.org/tex2img.php?eq=a%2B%28a%2Bd%29%2B%28a%2B2d%29%2B+...%2B%28a%2B%28n-1%29d%29+%3D+%5Cfrac%7Bn%7D%7B2%7D+%282a%2B%28n-1%29d%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)

### Geometric Progression

![equation](http://www.sciweavers.org/tex2img.php?eq=a%2Bar%2Bar%5E2%2B...%2Bar%5E%7Bn-1%7D+%3D+%5Cfrac%7Ba%28r%5En-1%29%7D%7B%28r-1%29%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)

### Sets

A set with `n` elements has `2^n` elements including empty set.

### Fibonacci Numbers

![equation](http://www.sciweavers.org/tex2img.php?eq=f%28n%29+%3D+%0D%0A+++++%5Cbegin%7Bcases%7D%0D%0A+++++++1+%26%5Cquad+n%3D1%5C%5C%0D%0A+++++++1+%26%5Cquad+n%3D2%5C%5C%0D%0A+++++++f%28n-1%29+%2B+f%28n-2%29+%26%5Cquad%5Ctext%7Botherwise.%7D+%5C%5C+%0D%0A+++++%5Cend%7Bcases%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)

There is a closed form formula to calculate nth Fibonacci number, called **Binet's Formula**.

![equation](http://www.sciweavers.org/tex2img.php?eq=f%28n%29+%3D+%0D%0A%5Cfrac%0D%0A%7B%281%2B%5Csqrt5%29%5En-%281-%5Csqrt5%29%5En%7D%0D%0A%7B2%5En%5Csqrt5%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)

### Logarithm

Useful property of logarithm is that,

![equation](http://www.sciweavers.org/tex2img.php?eq=%5Clog_kx+%3D+%5Ctext%7Btimes+we+have+to+divide+x+by+k+before+reaching+1%7D%5C%5C%0D%0A%5Clfloor%7B%5Clog_k%28x%29%2B1%7D+%5Crfloor+%3D+%5Ctext%7Bno+of+digits+in+x+when+written+in+base+k%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)

## Time Complexity

| Time Complexity | Description                                                  | Input Size(for 1s) |
| --------------- | ------------------------------------------------------------ | ------------------ |
| `O(1)`          | Constant time algorithm. Most likely a direct formula.       | `any`              |
| `O(log(n))`     | Algorithm which halves the input size at each step.          | `any`              |
| `O(sqrt(n))`    | Algorithm which search only until the middle of the input.   | `10^13`            |
| `O(n)`          | Algorithm which goes through each input a constant number of times. | `10^7`             |
| `O(nlog(n))`    | Algorithm which sorts the input or uses a data structure which takes `O(log n)` time for each input | `5*10^5`           |
| `O(n^2)`        | Algorithm which goes through all pairs in input.             | `3000`             |
| `O(n^3)`        | Algorithm which goes through all triplets in input.          | `200`              |
| `O(2^n)`        | Algorithm which goes through all subsets of input.           | `20`               |
| `O(n!)`         | Algorithm which goes through all permutations.               | `10`               |



