class Node:
    def __init__(self):
        self.links = [None]*27
        self.data = None

class Tries:
    def __init__(self):
        self.root = Node()

    def insert(self, key, data=None):

        current = self.root

        for char in key:
            index = self.calculate_ascii_index(char)

            if current.links[index] is None:
                current.links[index] = Node()

            current = current.links[index]
        
        if current.links[0] is None:
            current.links[0] = Node()

        current = current.links[0]
        current.data = data

    
    def reverse_insert(self, key, data=None):
        current = self.root

        for i in range(len(key)-1, -1, -1):
            index = self.calculate_ascii_index(key[i])

            if current.links[index] is None:
                current.links[index] = Node()

            current = current.links[index]
        
        if current.links[0] is None:
            current.links[0] = Node()

        current = current.links[0]
        current.data = data

    def calculate_ascii_index(self, char):
        return ord(char)-65+1
    
    def insert_rec(self, key, data):
        current = self.root
        self.insert_rec_aux(key, current, data, 0)
    
    def insert_rec_aux(self, key, current, data, pointer):
        if pointer == len(key):
            current.links[0] = Node()
            current.links[0].data = data
            return 
        
        index = self.calculate_ascii_index(key[pointer])

        if current.links[index] is None:
            current.links[index] = Node()

        self.insert_rec_aux(key, current.links[index], data, pointer+1)

    def insertAllSuffix(self, key):
        start = 0
        while start < len(key):
            suffix_len = len(key)-start
            curr = self.root
            curr.data = ""
            for i in range(start, len(key)):
                print(key[i])
                index = self.calculate_ascii_index(key[i])
                if curr.links[index] is None:
                    curr.links[index] = Node()
                curr.links[index].data = curr.data + key[i]
                curr = curr.links[index]
            if curr.links[0] is None:
                curr.links[0] = Node()
            curr.links[0].data = curr.data
            start += 1

    def insert_all_reverse_suffix(self, key):
        start = len(key)-1
        while start >= 0:
            # suffix_len = len(key)-start
            curr = self.root
            curr.data = ""
            for i in range(start, -1, -1):
                # print(key[i])
                index = self.calculate_ascii_index(key[i])
                if curr.links[index] is None:
                    curr.links[index] = Node()
                curr.links[index].data = curr.data + key[i]
                curr = curr.links[index]
            if curr.links[0] is None:
                curr.links[0] = Node()
            curr.links[0].data = curr.data
            start -= 1

    def find_substring_with_prefix(self, prefix):
        current = self.root

        for char in prefix:
            index = self.calculate_ascii_index(char)

            if current.links[index] is None:
                raise Exception(f"\"{prefix}\" does not exist.")

            current = current.links[index]

        # traverse from current
        return self.traverse(current)

    def traverse(self, root):
        res = []
        self.traverse_aux(root, res)
        return res
    
    def traverse_aux(self, curr, res):
        if curr is None:
            return
        
        if curr.links[0] is not None:
            res.append(curr.links[0].data)

        self.traverse_aux(curr.links[1], res)
        self.traverse_aux(curr.links[2], res)
        self.traverse_aux(curr.links[3], res)
        self.traverse_aux(curr.links[4], res)

    def insertAllprefix(self, key):
        end = len(key)
        while end > 0:
            # suffix_len = len(key)-start
            curr = self.root
            curr.data = ""
            for i in range(0, end):
                print(key[i])
                index = self.calculate_ascii_index(key[i])
                if curr.links[index] is None:
                    curr.links[index] = Node()
                curr.links[index].data = curr.data + key[i]
                curr = curr.links[index]
            if curr.links[0] is None:
                curr.links[0] = Node()
            curr.links[0].data = curr.data
            end -= 1


    def search(self, key):
        current = self.root

        for char in key:
            index = self.calculate_ascii_index(char)

            if current.links[index] is None:
                raise Exception(f"\"{key}\" does not exist.")

            current = current.links[index]
        
        if current.links[0] is None:
            raise Exception(f"\"{key}\" does not exist.")

        current = current.links[0]
        return current.data

if __name__ == "__main__":
    tries = Tries()
    tries.insert("ABC", 5)
    tries.insert("ABD", 6)
    tries.insert("CBD", 8)
    print(tries.search("ABC"))
    print(tries.search("CBD"))
    print(tries.search("ABD"))
    print("------------")
    tries.insertAllSuffix("ABCD")
    print("------------")
    print(tries.search("D"))
    print(tries.search("CD"))
    print(tries.search("BCD"))
    print("------------")
    tries.reverse_insert("ABCD", "reverse")
    print(tries.search("DCBA"))
    print("------------")
    tries.insert_all_reverse_suffix("AAABBB")
    print(tries.search("BBBAAA"))
    print(tries.search("BBAAA"))
    print(tries.search("BAAA"))
    print(tries.search("AAA"))
    print(tries.search("AA"))
    print(tries.search("A"))
    tries.insertAllSuffix("AAABBB")
    print(tries.search("AAABBB"))
    print(tries.search("AABBB"))
    print(tries.search("ABBB"))
    print(tries.search("BBB"))
    print(tries.search("BB"))
    print(tries.search("B"))
    print(tries.traverse(tries.root))
    print(tries.find_substring_with_prefix("A"))