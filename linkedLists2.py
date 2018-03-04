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
    
 
def reverse(linkedList):
    '''
    1) Start at the head of the linked list.
    2) Iterate over the list until "current" is None
    3) During each iteration, "reverse" the list by setting 
    the "next"(after) node of the current node to the
    "previous"(before) node
    
    Iteration process:
    4) 
        Set "previous"(before) as the current node - this is the node we just dealt with
        current as "next"(after) - move on to the next node to reverse
        "next"(after) as the node after that - this is the node we will need to reverse next
    5) When current becomes None, set the head of the list to the previous(before) node
    '''
    
    
    before = None
    current = linkedList.head
    after = current.after
    
    while current:
        current.after = before # reverse the pointer of the current node to point to the node that came before it
        before = current # current becomes the node we just finished reversing
        current = after # move on to the next node to reverse, this becomes the new current node
        if after: #True except for when we're on the last node
            after = after.after # this is the node we will be reversing next iteration
    linkedList.head = before
    return linkedList
        
lis = LinkedList()
lis.addNode(1)
lis.addNode(2)
lis.addNode(3)
lis.addNode(4)
lis.addNode(5)

print(lis)

lis2 = reverse(lis)
print(lis2)