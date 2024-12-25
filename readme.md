# Advent of Code 2022



## Links

- [aoc](https://adventofcode.com/)
- [hughcoleman github solutions](https://github.com/hughcoleman/advent-of-code/blob/main/2022)
- [David Singleton AOC Blog](https://blog.singleton.io/posts/2023-01-14-advent-of-code/)
- [reddit](https://www.reddit.com/r/adventofcode/)
- [coding tips and utils from mcpower](https://gist.github.com/mcpower/87427528b9ba5cac6f0c679370789661)


## What I am learning

Write less code - less code means fewer bugs.

Running jupyter: `uv run --with jupyter jupyter lab`

### Day 8: Treetop Tree House

I build up,down,left and right functions to check directions and a function to take until for part 2 line of sight calcuation. I learnt that you can:
- use numpy and rotate the array 90 degree and check. But you don't have to use numpy to rotate.
- keep a grid of scores for part 1 and part 2
- use [next and generators](https://realpython.com/introduction-to-python-generators/) to stop at a index number in an bool array 
- that bitwise operator tilde (~) doesn't work on list of bools but does on numpy's bool array. You can instead use not [link](https://stackoverflow.com/questions/13600988/python-tilde-unary-operator-as-negation-numpy-bool-array)

### 2024-01: Historian Hysteria

Extracting data from the txt files using `split()`. This will split on any whitespace, rather the `splitlines()` which is at the end of the line.

The unpackage operator (`*`) unpackages a list into function arguments or unpacks multiple values into a list:
```python
data = ['1', '2' ,'3' ,'4' ,'5']
[*map(int, data)] # [1, 2, 3, 4, 5]
```

List slicing using step size to take alternative elements: 
```python
data = [1, 2, 3, 4, 5, 6]
data[1::2] # [2, 4, 6]
```

Counting on lists:
```python
data = [0 ,0 ,1]
data.count(0) # 2
```

### 2024-02: Red-Nosed Reports

Rather than using zip to get current and next item, just use `d[i]` and `d[i+1]`.
Sets will return just the unique values from a list.
You can reverse a list by doing `d[::-1]` so don't need to build incrementing and decrementing comparisions.

### 2024-03 Mull It Over
