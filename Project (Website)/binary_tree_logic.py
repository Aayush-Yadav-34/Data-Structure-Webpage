class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def traverse(self):
        elements = []
        self._in_order_traversal(self.root, elements)
        return elements

    def _in_order_traversal(self, node, elements):
        if node:
            self._in_order_traversal(node.left, elements)
            elements.append(str(node.data))
            self._in_order_traversal(node.right, elements)

    def create_graph(self):
        from graphviz import Digraph
        dot = Digraph()
        try:
            self._add_edges(dot, self.root)
        except Exception as e:
            print(f"Error creating graph: {e}")
        return dot

    def _add_edges(self, dot, node):
        if node:
            dot.node(str(node.data))
            if node.left:
                dot.edge(str(node.data), str(node.left.data))
                self._add_edges(dot, node.left)
            if node.right:
                dot.edge(str(node.data), str(node.right.data))
                self._add_edges(dot, node.right)
