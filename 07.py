class Tree:
    def __init__(self, name, value):
        self.children = []
        self.name = name
        self.value = 0


    def add_child(self, name, value):
        self.children.append(Tree(name, value))

    


t = Tree("\\", 0)

t.add_child("b.txt", 14848514)
t.add_child("c.dat", 8504156)
t.add_child("a",0)
# t.a.add_child("f",29116)


print (t.children)
