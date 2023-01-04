#!/usr/bin/env python3
""" Day 07/2022: No Space Left On Device """


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
        return f"name: {self.name} size: {self.size} children_count: {str(len(self.children))} parent: {self.parent.name if self.parent else None}"

    def print_tree(self, prefix=""):
        print(prefix + repr(self))
        for child in self.children:
            child.print_tree(prefix + " " * 4)

    def traverse(self):
        total = 0
        for child in self.children:
            total += child.traverse()

        if len(self.children) == 0:
            return self.size
        else:
            print(self.name, total)
            return total

        

    # def traverse_and_sum(self):
    #     total = 0
    #     for child in self.children:
    #         if child.
    #     if self.children:


t = Tree("top", 0)
t.add_child("a", 1)
t.add_child("b", 2)
c = t.add_child("c", 0)
c.add_child("d", 4)
c.add_child("e", 5)


print(t)

# t.print_tree()
# t.traverse()


# top
#     a 1
#     b 2
#     c
#         d 4
#         e 5
