class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,element):
        self.queue.append(element)
    
    def dequeue(self):
        if not self.queue:
            return "Queue is empty!"
        return self.queue.pop(0)
    
    def peek(self):
        if not self.queue:
            return "Queue is empty!"
        return self.queue[0]
    
    def empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

queue = Queue()
queue.enqueue('1')
queue.enqueue('2')
queue.enqueue('3')
print("Queue elements are", queue.queue)
# print("Dequeue element is", queue.dequeue())
print("Peek element", queue.peek())
print("Is Queue empty?", queue.empty())
print("Queue size is", queue.size())