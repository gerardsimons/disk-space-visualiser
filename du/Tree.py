
from json import JSONEncoder

class Node(object):

    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = list()

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        """Define a non-equality test"""
        return not self.__eq__(other)

    def find_node(self, node_name):
        
        # Check the children recursively
        for child in self.children:

            if child.name == node_name:
                return child

            n = child.find_node(node_name)
            if n is not None:
                return n

        # Stop condition, nothing was found
        return None

    def add_node(self, node):
        self.children.append(node)

    def __str__(self):
        return "Node name : %r" % (self.name)

    def __repr__(self):
        return self.__str__()

    def print_tree(self):
        def print_tree_helper(node, depth):

            # print(node, depth)
            char = '-'
            indent_size = 8

            # min_depth = max(0, depth)
            # print(min_depth)
            indentation_str = " " * ((depth - 1) * (indent_size + 2))
            if depth:
                branch_str = "├" + char * indent_size
            else:
                branch_str = ""

            print("%s%s%r" % (indentation_str, branch_str, node.name))

            for child in node.children:
                # print("child " + child.name + " of", self.name)
                print_tree_helper(child, depth + 1)

        print_tree_helper(self, 0)

def print_tree(root):

    depth = 0

    # print(root.name)
    print_tree_helper(root, 0)

class NodeEncoder(JSONEncoder):

    def default(self, o):
        obj_dict = o.__dict__

        if not o.children:
            del obj_dict['children']

        if o.value is None:
            del obj_dict['value']

        return obj_dict

if __name__ == '__main__':

    ''' Some informal testing '''
    n = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n.add_node(Node(12))
    n.add_node(n2)
    n2.add_node(n3)
    n.add_node(Node(14))

    print(n.find_node(3))
    print(n.find_node(3) == n3)

    n.print_tree()

