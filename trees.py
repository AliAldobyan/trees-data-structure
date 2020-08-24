class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        if len(self.children) < 2:
            self.children.append(child)
            print(f"{child.name} is added to {self.name}")
        else:
            print(f"{child.name} is an orphan")


    def remove_child(self, node):
        self.children = [child for child in self.children if child is not node]


    def traverse(self):
        nodes = [self]
        while len(nodes) != 0:
            current_node = nodes.pop()
            print(current_node.name)
            nodes += current_node.children

    def get_child_with_name(self, name):

        for child in self.children:
            if child.name == name:
                return child
        return None




root = Node("Aldobyan")
full_name = input("enter child full name (done if finished): ")

while full_name != "done":
    current_child  = root

    names = full_name.split()[::-1]
    first_name = names.pop()
    last_name = names.pop(0)

    if current_child.name == last_name:
        if names:
            for name in names:
                child = current_child.get_child_with_name(name)
                if child:
                    current_child = child
                else:
                    new_child = Node(name)
                    current_child.add_child(new_child)
                    current_child = new_child
        current_child.add_child(Node(first_name))

    print("-"*70)
    full_name = input("enter child full name (done if finished): ")
root.traverse()
