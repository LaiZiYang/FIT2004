
class CircularQueue():
    """ Circular implementation of a queue with arrays.
    
    Attributes:
         length (int): number of elements in the stack (inherited)
         front (int): index of the element at the front of the queue
         rear (int): index of the first empty space at the oback of the queue
         array (ArrayR[T]): array storing the elements of the queue

    ArrayR cannot create empty arrays. So MIN_CAPCITY used to avoid this.
    """
    MIN_CAPACITY = 1 

    def __init__(self,max_capacity:int) -> None:
        self.length = 0
        self.front = 0
        self.rear = 0
        self.array = [None] * max(self.MIN_CAPACITY, max_capacity)


    def append(self, item) -> None:
        """ Adds an element to the rear of the queue.
        :pre: queue is not full
        :raises Exception: if the queueu is full
        """
        if self.is_full():
            raise Exception("Queue is full")

        self.array[self.rear] = item
        self.length += 1
        self.rear = (self.rear + 1) % len(self.array)

    def serve(self):
        """ Deletes and returns the element at the queue's front.
        :pre: queue is not empty
        :raises Exception: if the queue is empty
        """
        if self.is_empty(): 
            raise Exception("Queue is empty")

        self.length -= 1
        item = self.array[self.front] 
        self.front = (self.front+1) % len(self.array)
        return item 

    def is_full(self) -> bool:
        """ True if the queue is full and no element can be appended. """
        return len(self) == len(self.array)
 
    def clear(self) -> None:
        """ Clears all elements from the queue. """
        self.length = 0
        self.front = 0
        self.rear = 0

    def __len__(self):
        return self.length
    
    def is_empty(self) -> bool:
        """ True if the queue is empty. """
        return len(self) == 0

if __name__ == "__main__":
    q = CircularQueue(5)
    q.append(4)
    print(q.serve())
    q.append(3)
    print(q.serve())
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q.serve())
    print(q.serve())
    print(q.serve())
    print(q.serve())
    q.append(10)
    q.append(11)
    q.append(12)
    print(q.serve())
    print(q.serve())
    print(q.serve())