import re

from du.Tree import Node, NodeEncoder

def parse_du(du_text):

    # Split by newline
    lines = du_text.splitlines()

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

            # Extract each path part
            path_parts = path.split("/")

            if path_parts[0] == '':
                path_parts[0] = '/' # Starts from root

            # If no root is set, just take the first part, should be the same for all!
            if root is None:
                root = Node(path_parts[0])
            node = root

            for path_part in path_parts[1:]:
                    
                n = node.find_node(path_part)
                if n is not None: # Found the node already, skip and search next one
                    node = n
                else: # Does not exist yet, create it, and keep searching from the new node
                    new_node = Node(path_part)
                    node.add_node(new_node)
                    node = new_node

            node.value = size
    
    return root

if __name__ == '__main__':
    
    test_string = """
    0B    /.DocumentRevisions-V100/PerUID
    0B    /.DocumentRevisions-V100/PerUID/501
    0B    /.DocumentRevisions-V100/PerUID/502
    0B    /.DocumentRevisions-V100/purgatory
    """

    # test_string = """
    # 0B    /B/C
    # 0B    /B/D
    # 0B    /E/C
    # """

    import json

    res = parse_du(test_string)
    print(json.dumps(res, cls=NodeEncoder, indent=4))

    # print(json.dumps(res.__dict__))

