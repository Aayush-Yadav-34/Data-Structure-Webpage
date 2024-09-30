# priority_queue_logic.py

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data, priority):
        new_node = Node(data, priority)
        self.queue.append(new_node)
        self.queue.sort(key=lambda x: x.priority)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0).data

    def traverse(self):
        return " | ".join(f"{node.data} (Priority: {node.priority})" for node in self.queue)
