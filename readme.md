# Advent of Code 2022



## Links

- [aoc](https://adventofcode.com/)
- [hughcoleman github solutions](https://github.com/hughcoleman/advent-of-code/blob/main/2022)
- [David Singleton AOC Blog](https://blog.singleton.io/posts/2023-01-14-advent-of-code/)
- [reddit](https://www.reddit.com/r/adventofcode/)



## What I'm learning

Write less code - less code means fewer bugs.

### Day 8: Treetop Tree House

I build up,down,left and right functions to check directions and a function to take until for part 2 line of sight calcuation. I learnt that you can:
- use numpy and rotate the array 90 degree and check. But you don't have to use numpy to rotate.
- keep a grid of scores for part 1 and part 2
- use [next and generators](https://realpython.com/introduction-to-python-generators/) to stop at a index number in an bool array 
- that bitwise operator tilde (~) doesn't work on list of bools but does on numpy's bool array. You can instead use not [link](https://stackoverflow.com/questions/13600988/python-tilde-unary-operator-as-negation-numpy-bool-array)
