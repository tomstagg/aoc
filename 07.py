#!/usr/bin/env python3

class Tree:
    def __init__(self, name, type="dir", size:int = 0 ):
        self.children = []
        self.name = name
        self.type = type
        self.size = size


    def add_child(self, name, type, size):
        self.children.append(Tree(name, type, size))


    def print_tree(self):
        print(self.name)
        for child in self.children:
            child.print_tree()




    
t = Tree("*")
t.add_child("b.txt", "file", 1)
t.add_child("c.txt", "file", 1)
t.add_child("d.txt", "file", 1)


t.print_tree()

print(t.children[0].name)


