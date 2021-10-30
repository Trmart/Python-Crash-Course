"""This is a module created to define Node and DLL classes to make a doubly liked list"""
#Node class for a doubly linked list
class Node():
    
    def __init__(self,data=None):
        self.next = None #pointer to next
        self.prev = None #pointer to prev 
        self.data = data #data stored with node

class DLL():
    
    def __init__(self):
        self.head=None #head ptr

    def insert_at_front(self,new_data):
            """This Function Pushes a Node To the Front of a DoublyLinkedList"""
            
            #allocate memory for new node and store new_data
            new_node = Node(new_data)
            
            #assign head to new_node->next
            new_node.next = self.head
            
            #change prev of head to new_node 
            if(self.head is not None):
                self.head.prev = new_node

            #move the head to point to new_node
            self.head = new_node
    
    def insert_after_node(self,prev_node,data):
        """given the prev node, insert a new node after the given node"""
        
        #check to make sure that the prev node doesn't point to NULL
        if(prev_node is None):
            print('the given prev node cannot be NULL')
            exit(1)
        
        #allocate the new node, and store data
        new_node = Node(data)

        #make new_node.next point to prev.next
        new_node.next = prev_node.next

        #make prev node as prev of new_node
        prev_node.next = new_node.prev

        #make new node prev point to prev
        new_node.prev = prev_node

        #change next prev of new_node to new_node
        if(new_node.next):
            new_node.next.prev = new_node


    def insert_at_end(self,data):
        """appends new node at end of list """
        #allocate new node in memory and insert data
        new_node = Node(data)

        #if the linked list is empty, make the new_node the as head
        if(self.head is None):
            self.head = new_node
            return
        
        #make last point to self.head as temp ptr
        last = self.head

        #traverse the list until the end 
        while(last.next):
            last = last.next
        
        #assign new_node to next of last 
        last.next = new_node 

        #assign last to prev of new_node
        new_node.prev = last

        

    
    def insert_before_node(self,data,next_node):
        """inserts a new node before the given node sent in"""
        #check if the node sent in points to NULL
        if(next_node == None):
            print()
            return
        
        #allocate new node and insert data
        new_node = Node(data)

        #assign prev of next node to prev of new node
        new_node.prev = next_node.prev

        #assign new_node to prev of next_node
        next_node.prev = new_node

        #assign next_node to next of new node
        new_node.next = next_node

        if(new_node.prev is not None):
            new_node.prev.next = new_node
        else:
            self.head = new_node
            
        return self


    def print_list_forward(self,node):
        """prints out the data stored in a DoublyLinkedList"""
        while(node is not None):
            print(node.data)
            node = node.next

    def print_list_reverse(self,node):
        """prints the contents of a liked list in revered order"""
        
        while(node is not None):
            last = node
            node = node.next
        
        while(last is not None):
            print(last.data)
            last = last.prev
    
    def remove_node(self,data):
        """"""