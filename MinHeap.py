
from typing import *
from random import randint


class MinHeap:
    MIN_CAPACITY = 1

    def __init__(self, max_size, initial_array=None):
        self.max_size = max_size
        if initial_array is None:
            self.length = 0
        else:
            self.length = self.max_size = len(initial_array)

        self.array = [None] * (max(self.max_size, self.MIN_CAPACITY) + 1)

        if initial_array:
            self.heapify(initial_array)

    def heapify(self, array):
        for i in range(len(array)):
            self.array[i+1] = array[i]

        for i in range(self.length//2, 0, -1):
            self.sink(i)

    def heapify_graph(self, veitices):
        for i in range(len(veitices)):
            vertex = veitices[i]
            vertex.pos = i+1
            self.array[i+1] = vertex

        for i in range(self.length//2, 0, -1):
            self.sink(i)

    def rise(self, index):
        item = self.array[index]

        while index//2 >= 1 and item < self.array[index//2]:
            self.array[index] = self.array[index // 2]
            index = index//2

        self.array[index] = item

    def add(self, item):
        if self.is_full():
            raise IndexError('Heap is full')

        self.length += 1
        self.array[self.length] = item
        self.rise(self.length)

    def is_full(self):
        return self.length + 1== len(self.array)
    
    def is_empty(self):
        return self.length == 0

    def get_min_child(self, index):

        if index*2 == self.length or self.array[index*2] < self.array[index*2 + 1]:
            return index*2
        else:
            return index*2 + 1
        
    def sink(self, index):
        item = self.array[index]

        while index*2 <= self.length:
            min_child_index = self.get_min_child(index)
            if item > self.array[min_child_index]:
                self.array[index] = self.array[min_child_index]
                index = min_child_index
            else:
                break

        self.array[index] = item

    def serve(self):
        if self.length == 0:
            raise IndexError('Heap is empty')
        
        item = self.array[1]
        self.length -= 1

        if self.is_empty():
            return item
        else:
            self.array[1] = self.array[self.length + 1]
            self.sink(1)
            return item
class VerticesMinHeap:
    MIN_CAPACITY = 1

    def __init__(self, max_size, initial_array):
        self.max_size = max_size
        if initial_array is None:
            self.length = 0
        else:
            self.length = self.max_size = len(initial_array)

        self.array = [None] * (max(self.max_size, self.MIN_CAPACITY) + 1)

        if initial_array:
            self.heapify_graph(initial_array)

    def heapify(self, array):
        for i in range(len(array)):
            self.array[i+1] = array[i]

        for i in range(self.length//2, 0, -1):
            self.sink(i)

    def heapify_graph(self, vertices):
        for i in range(len(vertices)):
            vertex = vertices[i]
            vertex.pos = i+1
            self.array[i+1] = vertex

        for i in range(self.length//2, 0, -1):
            self.sink(i)

    def rise(self, index):
        item = self.array[index]

        while index//2 >= 1 and item.distance < self.array[index//2].distance:
            self.array[index] = self.array[index // 2]
            self.array[index].pos = index
            index = index//2

        self.array[index] = item
        self.array[index].pos = index

    def add(self, item):
        if self.is_full():
            raise IndexError('Heap is full')

        self.length += 1
        self.array[self.length] = item
        item.pos = self.length
        self.rise(self.length)

    def update(self, pos, distance):
        self.array[pos].distance = distance
        self.rise(pos)

    def is_full(self):
        return self.length + 1== len(self.array)
    
    def is_empty(self):
        return self.length == 0

    def get_min_child(self, index):

        if index*2 == self.length or self.array[index*2].distance < self.array[index*2 + 1].distance:
            return index*2
        else:
            return index*2 + 1
        
    def sink(self, index):
        item = self.array[index]

        while index*2 <= self.length:
            min_child_index = self.get_min_child(index)
            if item.distance > self.array[min_child_index].distance:
                self.array[index] = self.array[min_child_index]
                self.array[index].pos = index
                index = min_child_index
            else:
                break

        self.array[index] = item
        self.array[index].pos = index

    def serve(self):
        if self.length == 0:
            raise IndexError('Heap is empty')
        
        item = self.array[1]
        self.length -= 1

        if self.is_empty():
            return item
        else:
            self.array[1] = self.array[self.length + 1]
            self.array[1].pos = 1
            self.sink(1)
            return item

# if __name__ == '__main__':
    # initial_array = [5, 3, 7, 1, 2, 4, 6]
    # random_distances = [15, 78, 51, 1, 40, 77, 91]
    # # list of random vertices
    # vertices = [Vertex(i) for i in range(1, 8)]
    # # initialise random distance for each vertex
    # for i in range(len(vertices)):
    #     vertices[i].distance = random_distances[i]
    # # heap = MinHeap(len(initial_array), initial_array)
    # # print(heap.array)

    # heap = VerticesMinHeap(len(vertices), vertices)
    # distances = [vertex.distance for vertex in heap.array[1:]]
    # pos = [vertex.pos for vertex in heap.array[1:]]
    # print(pos)
    # print(distances)
    # print(heap.array)

    # heap.update(6, 50)
    # pos = [vertex.pos for vertex in vertices]
    # print(pos)
    # print(heap.array)