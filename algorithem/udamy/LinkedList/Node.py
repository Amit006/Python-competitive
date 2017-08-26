'''
Created on 16-Nov-2016

@author: FRODT
'''
class Node(object):
    
    def __init__(self,data):
        self.data =data;
        self.nextNode=None;
        
        
    def remove(self,data,previousnode):
        if self.data == data:
            previousnode.nextNode=self.nextNode;
            del self.data
            del self.nextNode
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data,self)