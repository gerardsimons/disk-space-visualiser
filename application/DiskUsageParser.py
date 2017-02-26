import re

from Tree import Node

def parse(du_text):

    # Split by newline
    lines = du_text.split("\n")

    # # Split by path seperator
    # for line in lines:
    #   line.split("")

    results = list()

    root = None

    for line in lines:
        print("LINE : '%s'" % line)
        pattern = re.compile(r"""\s*                
                                 (?P<size>\S*)      
                                 \s*(?P<path>\S*)   
                                 """, re.VERBOSE)

        
        match = pattern.match(line)

        size = match.group("size")
        path = match.group("path")
        # path = ''

        if len(size) and len(path):
            results.append((size, path))

            paths = path.split("/")
            print(paths)

            if paths[0] == '':
                paths[0] = '/' # Starts from root

            # root = 
            if root is None:
                root = Node(paths[0])
            node = root

            for path in paths[1:]:
                    
                n = node.find_node(path)
                if n is not None: # Found the node already
                    print(path + " exists.")
                    node = n
                else:
                    print("Adding", path, "to", node.value)
                    new_node = Node(path)
                    node.add_node(new_node)
                    node = new_node
    
    return root

if __name__ == '__main__':
    
    test_string = """
    0B    /.DocumentRevisions-V100/PerUID
    0B    /.DocumentRevisions-V100/PerUID/501
    0B    /.DocumentRevisions-V100/PerUID/502
    0B    /.DocumentRevisions-V100/purgatory
    """

    test_string = """
    0B    /B/C
    0B    /B/D
    0B    /E/C
    """

    import json

    res = parse(test_string)
    # print(res.children)
    # print(res.print_)
    print("TREE")
    res.print_tree()
    # print(json.dumps(res.__dict__))

