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