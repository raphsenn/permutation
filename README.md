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

#### For example:

```js
>>> from permutation.permutation import Permutation
>>> p = Permutation(2, 1, 3)
>>> p(1) 
2
>>> p(2)
1
>>> p(3)
3
>>> q = Permutation(1, 2)
>>> q(1)
1
>>> q(2)
2
```

### Cycle Notation of Sn
<p float="left">
   <img src="./res/math4.png">
</p>

#### For example:

```js
>>> from permutation.permutation import Permutation
>>> p = Permutation(5, 4, 1, 2, 6, 3, 7)
>>> p.to_cycle()
(1 5 6 3)(2 4)
>>> q = Permutation(1, 2, 3, 4, 5)
>>> q.to_cycle()
()
>>> print(p)
(1 5 6 3)(2 4)
```
