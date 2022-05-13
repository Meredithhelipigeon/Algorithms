# Python Cheat Sheet

## 1. Copy

- `copy.copy(x)` return a shallow copy of x
- `copy.deepcopy(x) `return a deep copy of x

Interesting finding:

- `x[:]` will returns a slicing window, which will do almost the same as `copy.deepcopy(x)` but quite fast!

