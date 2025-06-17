class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front=self.rear=new_node
            self.length+=1
            return
        self.rear.next=new_node
        self.rear=new_node
        self.length+=1

    def dequeue(self):
        if self.empty():
            print("Queue is empty.")
        temp = self.front
        self.front=temp.next
        self.length -= 1
        return temp.data

    def peek(self):
        if self.empty():
            return "Queue is empty."
        return self.front.data
    
    def empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def print_queue(self):
        temp=self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")
myQueue.print_queue()
# print("Dequeue: ", myQueue.dequeue())
print("Peek: ", myQueue.peek())
myQueue.print_queue()
print("isEmpty: ", myQueue.empty())
print("Size: ", myQueue.size())

