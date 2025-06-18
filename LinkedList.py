class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    #Insert value at the end of the linkedlist
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
    
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    #Insert value in the begining of the linkedlist
    def insert_at_first(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        node = Node(data,self.head)
        self.head = node

    #Insert value at an given index
    def insert_at(self,index,data):
        if index < 0 or index > self.length_ll():
            raise Exception("Invalid Index.")
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    # #Remove node by the value
    def remove_by_value(self,value):
        pass

    # #Remove node by the index
    def remove_by_index(self,index):
        pass

    #Remove node at the begining of the linkedlist
    def remove_at_first(self):
        if self.head is None:
            print("Linkedlist is empty.")
            return
        # itr = self.head
        # while itr:
        #     if itr.next is None:
        #         self.head = None
        #         break

    # #Remove node at the end of the linkedlist
    def remove_at_end(self):
        pass
            
    #Traverse through the linkedlist
    def print_ll(self):
        if self.head is None:
            print("LinkedList is empty.")
            return
        itr = self.head
        result = ''
        while itr:
            result += str(itr.data) + "-->"
            itr = itr.next
        print(result)

    #Length of the LinkedList
    def length_ll(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

ll = LinkedList()
# ll.insert_at_end(1)
# ll.insert_at_end(2)
# ll.insert_at_end(3)
# ll.insert_at_first(0)
# ll.insert_at(3,100)
# ll.length_ll()
# ll.remove_at_first()
ll.print_ll()