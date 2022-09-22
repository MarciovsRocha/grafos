#!/usr/bin/python

# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# ------------------------------------------------------------

class Node:
    value: int
    name: str
    l_child: None
    r_child: None
    parent_node: None

    def __init__(self, value: int, l_child=None, r_child=None, name: str = ''):
        self.l_child = l_child
        self.r_child = r_child
        self.value = value
        self.name = name


class BinarySearchTree:
    root: Node = None

    def __init__(self, root: Node = None):
        self.root = root

    # accepts Node
    def add_node(self, NewNode: Node):
        current_node = self.root
        if self.root is None:
            self.root = NewNode
            return self
        elif NewNode is not None:
            while True:
                if current_node.value >= NewNode.value:
                    if current_node.l_child is None:
                        NewNode.parent_node = current_node
                        current_node.l_child = NewNode
                        return self
                    else:
                        current_node = current_node.l_child
                else:
                    if current_node.r_child is None:
                        NewNode.parent_node = current_node
                        current_node.r_child = NewNode
                        return self
                    else:
                        current_node = current_node.r_child

    # remove higher node
    def list_higher_nodes(self, n: int = 1):
        current_node = self.root
        # reaches higher node
        while current_node.r_child is not None:
            current_node = current_node.r_child
        higher_nodes = []
        while n > len(higher_nodes):
            if (current_node.r_child is not None) and (current_node.r_child not in higher_nodes):
                current_node = current_node.r_child
            elif current_node not in higher_nodes:
                higher_nodes.append(current_node)
                if current_node.l_child is not None:
                    current_node = current_node.l_child
                else:
                    current_node = current_node.parent_node
            else:
                current_node = current_node.parent_node
        return higher_nodes
