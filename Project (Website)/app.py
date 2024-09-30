from flask import Flask, render_template, request, redirect, url_for, flash, Response
from queue_logic import Queue
from stack_logic import Stack
from linked_list_logic import LinkedList
from double_linked_list_logic import DoublyLinkedList
from priority_queue_logic import PriorityQueue
from binary_tree_logic import BinaryTree
from huffman_coding_logic import HuffmanCoding
from graph_dfs_logic import Graph as GraphDFS
from tsp_logic import TSP
from hash_table_chaining_logic import HashTableChaining
from graph_bfs_logic import GraphBFS  # Import the new Graph BFS class
import matplotlib.pyplot as plt
import networkx as nx
import pydot
from io import BytesIO
import heapq
from collections import defaultdict
from hash_table_no_collision_logic import HashTableNoCollision

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Instantiate your data structures
queue = Queue()
stack = Stack() 
linked_list = LinkedList()  
doubly_linked_list = DoublyLinkedList()
priority_queue = PriorityQueue()
binary_tree = BinaryTree()
huffman = HuffmanCoding()
graph_dfs = GraphDFS()
graph_bfs = GraphBFS()
tsp = TSP()
hash_table_chaining = HashTableChaining()
hash_table_no_collision = HashTableNoCollision()

@app.route('/')
def index():
    return render_template('index.html')

# Hash Table Without Collision Route
@app.route('/hash_table', methods=['GET', 'POST'])
def hash_table_app():
    if request.method == 'POST':
        action = request.form['action']
        value = request.form['value']  # Input value from the form
        
        try:
            if action == 'Insert' and value:
                hash_table_no_collision.insert(value)
                flash(f"Inserted {value}")
            elif action == 'Delete' and value:
                hash_table_no_collision.delete(value)
                flash(f"Deleted {value}")
            elif action == 'Search' and value:
                if hash_table_no_collision.search(value):
                    flash(f"Found {value}")
                else:
                    flash(f"{value} not found")
        except Exception as e:
            flash(str(e))

    # Traverse the hash table and pass it to the template
    table_items = hash_table_no_collision.traverse()
    return render_template('hash_table_no_collision_app.html', items=table_items)

# Doubly Linked List Application Route
@app.route('/doubly_linked_list', methods=['GET', 'POST'])
def doubly_linked_list_app():
    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'Insert at Beginning':
            item = request.form['item']
            if item:
                doubly_linked_list.insert_at_beginning(item)
                flash(f"Inserted {item} at the beginning.")
            else:
                flash("Please enter an item.")
        elif action == 'Insert at End':
            item = request.form['item']
            if item:
                doubly_linked_list.insert_at_end(item)
                flash(f"Inserted {item} at the end.")
            else:
                flash("Please enter an item.")
        elif action == 'Delete at Beginning':
            deleted_item = doubly_linked_list.delete_at_beginning()
            if deleted_item is not None:
                flash(f"Deleted {deleted_item} from the beginning.")
            else:
                flash("The list is empty.")
        elif action == 'Delete at End':
            deleted_item = doubly_linked_list.delete_at_end()
            if deleted_item is not None:
                flash(f"Deleted {deleted_item} from the end.")
            else:
                flash("The list is empty.")
        elif action == 'Traverse':
            elements = doubly_linked_list.traverse()
            flash(f"Doubly Linked List: {elements}")

        return redirect(url_for('doubly_linked_list_app'))

    return render_template('doubly_linked_list_app.html', items=doubly_linked_list.traverse())

# Priority Queue Application Route
@app.route('/priority_queue', methods=['GET', 'POST'])
def priority_queue_app():
    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'Enqueue':
            item = request.form['item']
            priority = request.form['priority']
            if item and priority.isdigit():
                priority_queue.enqueue(item, int(priority))
                flash(f"Enqueued {item} with priority {priority}.")
            else:
                flash("Please enter a valid item and priority.")
        elif action == 'Dequeue':
            dequeued_item = priority_queue.dequeue()
            if dequeued_item:
                flash(f"Dequeued item: {dequeued_item}")
            else:
                flash("The queue is empty.")
        elif action == 'Traverse':
            elements = priority_queue.traverse()
            flash(f"Priority Queue: {elements}")

        return redirect(url_for('priority_queue_app'))

    return render_template('priority_queue_app.html', items=priority_queue.traverse())

# Binary Tree Application Route
@app.route('/binary_tree', methods=['GET', 'POST'])
def binary_tree_app():
    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'Insert':
            item = request.form['item']
            if item:
                try:
                    binary_tree.insert(int(item))
                    flash(f"Inserted {item} into the binary tree.")
                except ValueError:
                    flash("Please enter a valid integer.")
            else:
                flash("Please enter an item.")
        elif action == 'Traverse':
            elements = binary_tree.traverse()
            flash(f"Binary Tree (In-Order): {', '.join(elements)}")

        return redirect(url_for('binary_tree_app'))

    return render_template('binary_tree_app.html', tree_elements=binary_tree.traverse())

# Render the binary tree graph
@app.route('/binary_tree_graph')
def binary_tree_graph():
    dot = binary_tree.create_graph()  # Generate the graph using Graphviz
    try:
        # Render the graph as a PNG image in memory
        img_io = BytesIO()
        dot.format = 'png'
        img_data = dot.pipe()
        img_io.write(img_data)
        img_io.seek(0)
        
        # Return the image as a response
        return Response(img_io.getvalue(), mimetype='image/png')
    
    except Exception as e:
        flash(f"Error generating graph: {str(e)}")
        return redirect(url_for('binary_tree_app'))


# Existing Queue Application Route
@app.route('/queue', methods=['GET', 'POST'])
def queue_app():
    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'Enqueue':
            item = request.form['item']
            if item:
                queue.enqueue(item)
                flash(f"Enqueued item: {item}")
            else:
                flash("Please enter an item to enqueue.")
        elif action == 'Dequeue':
            dequeued_item = queue.dequeue()
            if dequeued_item is not None:
                flash(f"Dequeued item: {dequeued_item}")
            else:
                flash("Queue is empty.")
        elif action == 'Peek':
            peeked_item = queue.peek()
            flash(f"Peeked item: {peeked_item}")
        elif action == 'Size':
            size = queue.size()
            flash(f"Queue size: {size}")
        return redirect(url_for('queue_app'))

    return render_template('queue_app.html', queue_items=queue.items)

# New Stack Application Route
@app.route('/stack', methods=['GET', 'POST'])
def stack_app():
    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'Push':
            item = request.form['item']
            if item:
                stack.push(item)
                flash(f"Pushed item: {item}")
            else:
                flash("Please enter an item to push.")
        elif action == 'Pop':
            popped_item = stack.pop()
            if popped_item is not None:
                flash(f"Popped item: {popped_item}")
            else:
                flash("Stack is empty")
        elif action == 'Peek':
            peeked_item = stack.peek()
            if peeked_item is not None:
                flash(f"Top item: {peeked_item}")
            else:
                flash("Stack is empty")
        elif action == 'Size':
            size = stack.size()
            flash(f"Stack size: {size}")

        return redirect(url_for('stack_app'))

    return render_template('stack_app.html', stack_items=stack.items)

# Linked List Application Route
@app.route('/linked_list', methods=['GET', 'POST'])
def linked_list_app():
    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'Insert at Beginning':
            item = request.form['item']
            if item:
                linked_list.insert_at_beginning(item)
                flash(f"Inserted {item} at the beginning.")
            else:
                flash("Please enter an item.")
        elif action == 'Insert at End':
            item = request.form['item']
            if item:
                linked_list.insert_at_end(item)
                flash(f"Inserted {item} at the end.")
            else:
                flash("Please enter an item.")
        elif action == 'Delete at Beginning':
            deleted_item = linked_list.delete_at_beginning()
            if deleted_item is not None:
                flash(f"Deleted {deleted_item} from the beginning.")
            else:
                flash("The linked list is empty.")
        elif action == 'Delete at End':
            deleted_item = linked_list.delete_at_end()
            if deleted_item is not None:
                flash(f"Deleted {deleted_item} from the end.")
            else:
                flash("The linked list is empty.")
        elif action == 'Traverse':
            elements = linked_list.traverse()
            flash(f"Linked List: {elements}")

        return redirect(url_for('linked_list_app'))

    return render_template('linked_list_app.html', linked_list_items=linked_list.traverse())

# Huffman Coding Route
@app.route('/huffman', methods=['GET', 'POST'])
def huffman():
    huffman_coding = HuffmanCoding()
    encoded_text = None
    graph_image = None

    if request.method == 'POST':
        text = request.form['text']

        try:
            # Encode the input text
            encoded_text = huffman_coding.compress(text)
            print(f"Encoded Text: {encoded_text}")  # Debug: Check encoded text

            # Create the Huffman Tree visualization
            if huffman_coding.heap:  # Check if heap is not empty
                graph = huffman_coding.create_graph()
                graph_image = graph.pipe(format='png')
                print("Graph generated successfully.")  # Debug: Check graph creation
            else:
                flash("No graph available: Heap is empty.")

        except ValueError as e:
            flash(str(e))  # Display the error message
            print(f"Error: {str(e)}")  # Debug: Check for errors

    return render_template('huffman_app.html', encoded_text=encoded_text, graph_image=graph_image)

@app.route('/huffman_graph')
def huffman_graph():
    return "No graph available", 404  # Fallback if no graph is generated

# Graph DFS Route
@app.route('/graph_dfs', methods=['GET', 'POST'])
def graph_dfs_app():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'Add Vertex':
            vertex = request.form['vertex']
            graph_dfs.add_vertex(vertex)
        elif action == 'Add Edge':
            v1, v2 = request.form['v1'], request.form['v2']
            graph_dfs.add_edge(v1, v2)
        elif action == 'Remove Vertex':
            vertex = request.form['vertex']
            graph_dfs.remove_vertex(vertex)
        elif action == 'Remove Edge':
            v1, v2 = request.form['v1'], request.form['v2']
            graph_dfs.remove_edge(v1, v2)
        elif action == 'DFS':
            start = request.form['start']
            result = graph_dfs.dfs(start)
            flash(f"DFS result: {', '.join(result)}")
        return redirect(url_for('graph_dfs_app'))
    return render_template('graph_dfs_app.html')

@app.route('/graph_dfs_visualization')
def graph_dfs_visualization():
    dot = graph_dfs.create_graph()
    img_io = BytesIO()
    dot.format = 'png'
    img_data = dot.pipe()
    img_io.write(img_data)
    img_io.seek(0)
    return Response(img_io.getvalue(), mimetype='image/png')

@app.route('/graph_bfs', methods=['GET', 'POST'])
def graph_bfs_app():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'Add Vertex':
            vertex = request.form['vertex']
            graph_bfs.add_vertex(vertex)
        elif action == 'Add Edge':
            v1, v2 = request.form['v1'], request.form['v2']
            graph_bfs.add_edge(v1, v2)
        elif action == 'Remove Vertex':
            vertex = request.form['vertex']
            graph_bfs.remove_vertex(vertex)
        elif action == 'Remove Edge':
            v1, v2 = request.form['v1'], request.form['v2']
            graph_bfs.remove_edge(v1, v2)
        elif action == 'BFS':
            start = request.form['start']
            result = graph_bfs.bfs(start)
            flash(f"BFS result: {', '.join(result)}")
        return redirect(url_for('graph_bfs_app'))
    return render_template('graph_bfs_app.html')

@app.route('/graph_bfs_visualization')
def graph_bfs_visualization():
    dot = graph_bfs.create_graph()
    img_io = BytesIO()
    dot.format = 'png'
    img_data = dot.pipe()
    img_io.write(img_data)
    img_io.seek(0)
    return Response(img_io.getvalue(), mimetype='image/png')


# TSP Route
@app.route('/tsp', methods=['GET', 'POST'])
def tsp_app():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'Add City':
            city = request.form['city']
            tsp.add_city(city)
            flash(f"Added city: {city}")
        elif action == 'Remove City':
            city = request.form['city']
            tsp.remove_city(city)
            flash(f"Removed city: {city}")
        elif action == 'Add Edge':
            city1 = request.form['city1']
            city2 = request.form['city2']
            distance = float(request.form['distance'])
            tsp.add_edge(city1, city2, distance)
            flash(f"Added edge: {city1} - {city2} (distance: {distance})")
        elif action == 'Solve':
            path, distance = tsp.solve_tsp()
            flash(f"Shortest path: {' -> '.join(path)}, Total distance: {distance:.2f}")
        return redirect(url_for('tsp_app'))
    return render_template('tsp_app.html', cities=tsp.cities, edges=tsp.edges)

@app.route('/tsp_visualization')
def tsp_visualization():
    dot = tsp.create_graph()
    img_io = BytesIO()
    dot.format = 'png'
    img_data = dot.pipe()
    img_io.write(img_data)
    img_io.seek(0)
    return Response(img_io.getvalue(), mimetype='image/png')

# Hash Table with Chaining Route
@app.route('/hash_table_chaining', methods=['GET', 'POST'])
def hash_table_chaining_app():
    if request.method == 'POST':
        action = request.form['action']
        value = request.form['value']  # Input value from the form
        
        if action == 'Insert' and value:
            hash_table_chaining.insert(value)
            flash(f"Inserted {value}")
        elif action == 'Delete' and value:
            hash_table_chaining.delete(value)
            flash(f"Deleted {value}")
        elif action == 'Search' and value:
            if hash_table_chaining.search(value):
                flash(f"Found {value}")
            else:
                flash(f"{value} not found")
    
    # Traverse the hash table and pass it to the template
    table_items = hash_table_chaining.traverse()
    return render_template('hash_table_chaining_app.html', items=table_items)

if __name__ == "__main__":
    app.run(debug=True)