## Stacks are better for tasks where immediacy matters, but if older messages are delivered slowly, 
## it doesn't matter. One example is a social network like Twitter -- 
## new tweets matter much more than older tweets, and showing them should be prioritized. 
## Thus you'd want to process and show newer tweets faster if your system was overloaded, 
## but could afford to ignore older ones for a while.

## Queues are better for tasks where consistency matters. 
## An example is ordering delivery with a tool like Seamless. 
## Seamless can't just ignore older orders, so they need to process everything with a queue to ensure fairness.


class Stack():
    def __init__(self):
        self.items = []
       
    def push(self, item):
        self.items.insert(0, item)
       
    def pop(self):
        return self.items.pop(0)
       
    def count(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()







class Queue():
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop(0)
    
    def count(self):
        return len(self.items)

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()




#queues:

#Are generally best when you want all tasks processed at about the same pace
#Have a fairly low maximum wait time for processing tasks

#stacks:

#Are generally best when you want tasks processed very quickly if possible, but are okay waiting around for a while if not.
#Have a fairly high maximum wait time.