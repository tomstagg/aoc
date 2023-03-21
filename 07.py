#!/usr/bin/env python3
""" Day 07/2022: No Space Left On Device """


"""I built a tree to do this - it was my first attempt.
First created the tree structure parsed on the instructions. 
Second sumed the files up the the parent directory level.
Third populated an array of directory totals from top to bottom.
Used this to find the answers"""

class Tree:
    def __init__(self, name, size=0, parent=None):
        self.name = name
        self.children = []
        self.size = size
        self.parent = parent
        self.id = f"{self.name} {self.size}, {str(len(self.children))}"

    def add_child(self, name, size):
        tree = Tree(name, size, parent=self)
        self.children.append(tree)
        return tree

    def __repr__(self) -> str:
        return f"{self.name} size:{self.size}"

    def print_tree(self, prefix=""):
        print(prefix + repr(self))
        for child in self.children:
            child.print_tree(prefix + " " * 4)


data = open("./resources/07_input.txt").read().splitlines()


def populate_tree():
    parent_node = None
    for cmd in data:
        # print (cmd)
        if cmd.startswith("$ cd /"):
            node = Tree("/")
            parent_node = node
            continue
        if cmd.startswith("dir"):
            name = cmd.split(" ")[-1]
            node.add_child(name, 0)
            continue
        if cmd.startswith("$ cd .."):
            node = node.parent
        if cmd.startswith("$ cd"):
            dirname = cmd.split(" ")[-1]
            for n in node.children:
                if n.name == dirname:
                    node = n
                    break
            continue
        if not cmd.startswith("$ ls"):
            name = cmd.split(" ")[1]
            size = int(cmd.split(" ")[0])
            node.add_child(name, size)

    return parent_node


def sum_files(node):
    total = 0
    if len(node.children) > 0:
        for child in node.children:
            total += sum_files(child)
        node.size = total
        return total
    else:
        return node.size


def traverse(node):
    if len(node.children) > 0:
        totals.append(node.size)
    for child in node.children:
        traverse(child)

full = populate_tree()
sum_files(full)
full.print_tree()

totals = []
traverse(full)

print("part 1:", sum([v for v in totals if v <= 100000]))
print("part 2:", min([v for v in totals if v >= totals[0] - 40000000]))
