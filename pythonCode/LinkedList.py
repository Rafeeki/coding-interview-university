# LinkedList that has head and tail node objects, as well as a size component
from Node import Node
class LinkedList(object):
    
    def __init__(self):
        self.head_ = None
        self.tail_ = None
    
    def set_head(self, head_node):
        self.head_ = head_node
        
    def set_tail(self, tail_node):
        self.tail_ = tail_node
    
    def __len__(self):
        count = 0
        current = self.head_
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def __str__(self):
        current = self.head_
        output = ""
        while current:
            output += str(current) + " -> "
            current = current.get_next()
        return output
    
    def empty(self):
        if (self.head_): return False
        else: return True
    
    def pop_front(self):
        if (self.head_): self.head_ = self.head_.get_next()
        else: raise IndexError("Unable to pop from empty list")
    
    def pop_back(self):
        if (self.tail_): 
            self.tail_ = self.tail_.get_prev()
            self.tail_.set_next(None)
        else: raise IndexError("Unable to pop from empty list")
    
    def contains(self, value):
        found = False
        current = self.head_
        while current and not found:
            if (current.get_data() == value): found = True
            else: current = current.get_next()
        return found
    
    def value_at(self, index):
        count = 0
        current = self.head_
        if (index < len(self) or index < 0):
            while count < index:
                count += 1
                current = current.get_next()
            return current.get_data()
        else: raise IndexError("Index is out of bounds")
            
    def front(self):
        return self.head_.get_data()
    
    def back(self):
        return self.tail_.get_data()
    
    def push_front(self, value):
        node = Node(value)
        node.set_next(self.head_)
        self.set_head(node)
    
    def push_back(self, value):
        node = Node(value)
        if (self.tail_): 
            self.tail_.set_next(node)
            node.set_prev(self.tail_)
        else: 
            current = self.head_
            if not current: 
                self.head_ = node
                return
            while current.get_next():
                current = current.get_next()
            current.set_next(node)
        self.set_tail(node)
        
    def erase(self, index):
        current = self.head_
        prev = None
        count = 0
        if (index < len(self) or index < 0):
            while count < index:
                count += 1
                prev = current
                current = current.get_next()
            if prev: prev.set_next(current.get_next())
            else: self.head_ = current.get_next()
        else: raise IndexError("Index is out of bounds")
    
    def insert(self, value, index):
        current = self.head_
        node = Node(value)
        prev = None
        count = 0
        if (index < len(self) or index < 0):
            while count < index:
                count += 1
                prev = current
                current = current.get_next()
            if prev: 
                prev.set_next(node)
                node.set_prev(prev)
                node.set_next(current)
                current.set_prev(node)
            else: 
                self.head_.set_next(node)
                node.set_prev(self.head_)
                node.set_next(current)
                current.set_prev(node)
        else: raise IndexError("Index is out of bounds")
    
    def remove_value(self, value):
        current = self.head_
        prev = None
        while current:
            if (current.get_data() == value):
                if prev: prev.set_next(current.get_next())
                else: self.head_ = current.get_next()
            prev = current
            current = current.get_next()