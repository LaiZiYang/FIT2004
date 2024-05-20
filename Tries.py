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

    def calculate_ascii_index(self, char):
        return ord(char)-65+1

    def build_suffix_tries(self, key):
        start = 0
        while start < len(key):

            curr = self.root

            for i in range(start, len(key)):
                index = self.calculate_ascii_index(key[i])

                if curr.links[index] is None:
                    curr.links[index] = Node()

                if curr.links[index].data is None:
                    curr.links[index].data = [start]
                else:
                    curr.links[index].data.append(start)

                curr = curr.links[index]

            if curr.links[0] is None:
                curr.links[0] = Node()

            curr.links[0].data = [start, len(key)-1]
            start += 1

    def search_substring(self, key):
        
        current = self.root

        for char in key:
            index = self.calculate_ascii_index(char)

            if current.links[index] is None:
                raise Exception("substring does not exist.")

            current = current.links[index]
        return current

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
    # tries.insert("ABC", 5)
    # tries.insert("ABD", 6)
    # tries.insert("CBD", 8)
    # print(tries.search("ABC"))
    # print(tries.search("CBD"))
    # print(tries.search("ABD"))
    # print("------------")
    # tries.insertAllSuffix("ABCD")
    # print("------------")
    # print(tries.search("D"))
    # print(tries.search("CD"))
    # print(tries.search("BCD"))
    # print("------------")
    # tries.reverse_insert("ABCD", "reverse")
    # print(tries.search("DCBA"))
    # print("------------")
    # tries.insert_all_reverse_suffix("AAABBB")
    # print(tries.search("BBBAAA"))
    # print(tries.search("BBAAA"))
    # print(tries.search("BAAA"))
    # print(tries.search("AAA"))
    # print(tries.search("AA"))
    # print(tries.search("A"))
    tries.insertAllSuffix("AAABBBCCCAA")
    # print(tries.search("AAABBBCCC"))
    # print(tries.search("AABBBCCC"))
    # print(tries.search("ABBBCCC"))
    # print(tries.search("BBBCCC"))
    # print(tries.search("BBCCC"))
    # print(tries.search("BCCC"))
    print(tries.traverse(tries.root))
    print("---------------------------")
    print(tries.find_substring_with_prefix("AA"))
    print(tries.find_substring_with_prefix("BB"))
    print(tries.list_all_starting_index_with_prefix("AA"))
    print(tries.list_all_starting_index_with_prefix("AB"))
    print(tries.list_all_starting_index_with_prefix("BB"))
    print(tries.list_all_starting_index_with_prefix("BC"))
    print(tries.list_all_starting_index_with_prefix("CC"))
    print(tries.list_all_starting_index_with_prefix("A"))
    print(tries.list_all_starting_index_with_prefix("B"))
    print(tries.list_all_starting_index_with_prefix("C"))
    print(tries.list_all_starting_index_with_prefix("AAA"))
    print(tries.list_all_starting_index_with_prefix("BBB"))
    print(tries.list_all_starting_index_with_prefix("CCC"))