class QueueArray:

    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        return self.queue.append(val)

    def length(self):
        return len(self.queue)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Is Empty")
        else:
            self.queue.pop(0)
            return self.queue

    def first(self):
        if len(self.queue) == 0:
            print("Queue Is Empty")
        else:
            return self.queue[0]

    def isempty(self):
        if len(self.queue) == 0:
            print("Queue Is Empty")
        else:
            return "Not Empty"

queue1 = QueueArray()
queue1.enqueue(10)
queue1.enqueue(11)
queue1.enqueue(12)
print(queue1.queue)
print(queue1.isempty())
print(queue1.dequeue())
print(queue1.length())
print(queue1.first())
print(queue1.dequeue())
print(queue1.dequeue())
print(queue1.isempty())


