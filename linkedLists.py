# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 22:01:54 2018

@author: eccrawford
"""

class LinkedList:
    
    
    # linkedList constructor
    def __init__(self):
        self.head = None
        self.size = 0
        
    def getSize(self):
        return self.size
    
            
    def addNode(self, value):
        node = Node(value)
    
        if self.head == None: #linked list is empty
            self.head = node
            self.size = 1
        else:
            node.after = self.head #make the new node point to the head of the rest of the linked list
            node.after.before = node #the new node now comes before the rest of the linked list
            self.head = node # the new head of the linked list is the new node
            self.size+=1
    
    def deleteNode(self, node):
        if node.before == None: # head of the list
            self.head = node.after
        else:
            temp = node.before
            node.before.after = node.after
            node.before = temp
        self.size-=1
        
    def traverse(self, value):
        node = self.head
        if node != None:
            while node.after != None:
                if node.value == value:
                    return node
                node = node.after
            if node.value == value:
                return node
        return None
    
    
    def __str__(self):
        current = self.head
        lis = "["
        while current:
            if len(lis)==1:
                lis = lis +str(current.value)
            else:
                lis = lis + ","+str(current.value)
            current = current.after
        lis = lis + "]"
        return lis
        
class Node:
    
    # Node constructor
    def __init__(self, value):
        #initialize the value of a node and its pointer
        self.value = value
        self.after = None
        self.before = None
    
                
        
lis = LinkedList()
lis.addNode(1)
lis.addNode(2)
lis.addNode(3)

print(lis)
print(lis.getSize())
lis.deleteNode(lis.traverse(3))
print(lis)
print(lis.getSize())