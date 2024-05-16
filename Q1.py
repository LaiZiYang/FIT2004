from Tries import Tries

class OrfFinder:

    def __init__(self, genome: str):
        self.genome = genome
        self.prefix_tries = Tries().insert_all_reverse_suffix(genome)
        self.suffix_tries = Tries().insertAllSuffix(genome)

    def find(self, start: str, end: str):
        pass
        #search all strings with start
        #search all strings with end
        # 