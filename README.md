# permutation
This Python library provides a versatile implementation of permutations in the context of abstract algebra. Specifically, it focuses on permutations as elements of symmetric groups defined over finite sets. The symmetric group's operation is based on the composition of functions, with elements representing bijections from a set to itself.

## Symmetric Group
<p float="left">
   <img src="./res/math1.png">
</p>

### (i) Symmetric Group
<p float="left">
   <img src="./res/math2.png">
</p>

### (ii) Symetric Group on *n* Digits
<p float="left">
   <img src="./res/math3.png">
</p>

### Cycle Notation of Sn
<p float="left">
   <img src="./res/math4.png">
</p>

## How to Use
### Examples
#### Create a Permutation
```js
>>> from permutation.permutation import Permutation
>>> p = Permutation(5, 4, 3, 2, 1)
>>> p(1) 
1
>>> p(2)
4
>>> p(3)
3
>>> p(4)
2
>>> p(5)
1
>>> p.to_cycle()
(1 5)(2 4)
>>> q = Permutation(5, 4, 1, 2, 6, 3, 7)
>>> q.to_cycle()
(1 5 6 3)(2 4)
```
