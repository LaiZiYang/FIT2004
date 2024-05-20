from Tries import Tries

class OrfFinder:

    def __init__(self, genome: str):
        self.genome = genome
        self.suffix_tries = Tries()
        self.suffix_tries.build_suffix_tries(genome)

    def find(self, start: str, end: str):
        list1 = None
        list2 = None
        
        try:
            list1 = self.suffix_tries.search_substring(start).data
        except:
            list1 = []
        try:
            list2 = self.suffix_tries.search_substring(end).data
        except:
            list2 = []
        res = []

        for prefix_start_index in list1:
            for suffix_start_index in list2:
                if (prefix_start_index + len(start) - 1) < suffix_start_index:
                    found = ""
                    for c in range(prefix_start_index, suffix_start_index + len(end)):
                        found = found + self.genome[c]
                    res.append(found)
        return res

if __name__ == "__main__":
    gnome = OrfFinder("BACACA")
    print(gnome.find("B", "A"))