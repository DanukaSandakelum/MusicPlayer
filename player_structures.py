import heapq
import os

class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.current = None
        self.size = 0

    def add_song(self, song_path):
        new_node = Node(song_path)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.current =self.head
        else:
            last = self.head.prev

            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

        self.size += 1

    def next_song(self):
        if self.current is None:
            return None
        
        self.current = self.current.next
        return self.current.data
    
    def prev_song(self):
        if self.current is None:
            return None

        self.current = self.current.prev
        return self.current.data
    
    def get_current_song(self):

        if self.current is None:
            return None
        return self.current.data
    
    def display_playlist(self):
        if self.head is None:
            print("list is empty")
            return None
        current = self.head
        for i in range(self.size):
            marker = " ->" if current == self.current else ""
            print(f"{i+1}. {os.path.basename(current.data)}{marker}")
            current = current.next

class Stack:
    def __init__(self):
        self.items =[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

class HuffmanNode:
    def __init__(self,char,freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self,other):
        return self.freq < other.freq
    
class HuffmanTree:
    def __init__(self,text):
        self.text = text
        self.code = {}
        self.root = self.build_tree()
        self.build_code(self.root, "")

    def build_tree(self):
        frequency ={}
        for char in self.text:
            frequency[char] = frequency.get(char,0) +1

        priorit_queue=[HuffmanNode(char,frequency)for char ,frequency in frequency.items()]
        heapq.heapify(priorit_queue)

        while len(priorit_queue) >1:

            left = heapq.heappop(priorit_queue)
            right = heapq.heappop(priorit_queue)

            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(priorit_queue, merged)

        return priorit_queue[0]
    
    def build_code(self,node, current_code):
        if node is None:
            return

        if node.char is not None:
            self.code[node.char] = current_code
            return

        self.build_code(node.left, current_code + "0")
        self.build_code(node.right, current_code + "1")
    def encode(self):
        encoded_text = ""
        for char in self.text:
            encoded_text += self.codes[char]
        return encoded_text
    
    def decode(self, encoded_text):
        decoded_text = ""
        current_node = self.root
        
        for bit in encoded_text:
            if bit == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right
            
            if current_node.char is not None:
                decoded_text += current_node.char
                current_node = self.root
        
        return decoded_text