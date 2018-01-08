# Node for a doubly-linked list, can be a singly-linked list if prev is left empty
class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data_ = data
        self.next_ = next
        self.prev_ = prev
    
    def get_data(self):
        return self.data_
    
    def set_data(self, data):
        self.data_ = data
        
    def get_next(self):
        return self.next_
    
    def set_next(self, next):
        self.next_ = next
    
    def get_prev(self):
        return self.prev_
    
    def set_prev(self, prev):
        self.prev_ = prev
    
    def __str__(self):
        return str(self.data_)