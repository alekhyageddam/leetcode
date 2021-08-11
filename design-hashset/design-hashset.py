
#Implement a hash table using the linekd list approach. Common choice of hash function is the modulus operator
#i.e. hash = value mod base
#Essentially, we are implementing a LinkedList that does not contain any duplicate.
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
        
    def hash(self,key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        #first find bucket index then insert key
        bucketIndex = self.hash(key)
        self.bucketArray[bucketIndex].insert(key)
        

    def remove(self, key: int) -> None:
        bucketIndex = self.hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucketIndex = self.hash(key)
        return self.bucketArray[bucketIndex].exists(key)
        

class Node:
    def __init__(self,value,nextNode=None):
        self.value = value
        self.next = nextNode
        
class Bucket:
    def __init__(self):
        self.head = Node(0) 
        
    def insert(self,newValue):
        #if the new value does not exist, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            #set the new head
            self.head.next = newNode
            
    def delete(self,value):
        prev = self.head
        curr = self.head.next 
        while curr is not None:
            if curr.value == value:
                prev.next = curr.next 
                return 
            prev = curr
            curr = curr.next 
    
    def exists(self,value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                return True 
            curr = curr.next 
        return False
    
    
        
        
        
        
        
        
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)