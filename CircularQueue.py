class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return
        
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
        
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        elif self.rear >= self.front:
            print("Elements in the circular queue are:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            print("Elements in the circular queue are:", end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")


if __name__ == "__main__":
    q = CircularQueue(5)
    q.enqueue(14)
    q.enqueue(22)
    q.enqueue(13)
    q.enqueue(-6)
    q.display()
    print("Deleted value =", q.dequeue())
    print("Deleted value =", q.dequeue())
    print("Deleted value =", q.dequeue())
    print("Deleted value =", q.dequeue())
    q.display()
    q.enqueue(9)
    q.enqueue(20)
    q.enqueue(5)
    q.display()
    q.enqueue(20)
    q.display()
    q.dequeue()