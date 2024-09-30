import heapq
from graphviz import Digraph

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            frequency[character] = frequency.get(character, 0) + 1
        return frequency

    def make_heap(self, frequency):
        for key in frequency:
            node = HuffmanNode(key, frequency[key])
            heapq.heappush(self.heap, node)
        print(f"Heap after making: {[node.char for node in self.heap]}")  # Debugging

    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)
        print("Merged nodes into Huffman Tree.")  # Debugging

    def make_codes_helper(self, root, current_code):
        if root is None:
            return
        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        if len(self.heap) == 0:
            raise ValueError("The heap is empty. Unable to create codes.")
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)
        print(f"Generated Huffman Codes: {self.codes}")  # Debugging

    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def compress(self, text):
        if not text:
            raise ValueError("Input text is empty.")
        frequency = self.make_frequency_dict(text)
        self.make_heap(frequency)
        self.merge_nodes()
        self.make_codes()
        encoded_text = self.get_encoded_text(text)
        return encoded_text

    def decompress(self, encoded_text):
        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""
        return decoded_text

    def create_graph(self):
        if len(self.heap) == 0:
            raise ValueError("No Huffman tree available for visualization.")
        dot = Digraph()
        root = self.heap[0]
        self._add_nodes_to_graph(root, dot)
        return dot

    def _add_nodes_to_graph(self, node, dot):
        if node is None:
            return
        dot.node(str(id(node)), f"{node.char if node.char else ''}\n{node.freq}")
        if node.left:
            dot.edge(str(id(node)), str(id(node.left)), '0')
            self._add_nodes_to_graph(node.left, dot)
        if node.right:
            dot.edge(str(id(node)), str(id(node.right)), '1')
            self._add_nodes_to_graph(node.right)
