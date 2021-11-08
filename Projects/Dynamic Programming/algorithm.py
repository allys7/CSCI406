class Algorithm:
    def init_table(self):
        self.table = [[None] * (self.targets+1) for _ in range(self.pumpkins+1)]
    
    def __init__(self, pumpkins: int, targets: int):
        self.recursive_counter = 0
        self.dynamic_counter = 0
        self.pumpkins = pumpkins
        self.targets = targets
        self.init_table()

    def print_table(self):
        for r in range(self.pumpkins):
            for c in range(self.targets):
                print(self.table[r][c], end="\t")
            print()

    def recursive(self, p: int, t: int) -> int:
        self.recursive_counter += 1
        if (t == 0 or t == 1):
            return t 
        if (p == 1):
            return t
        
        results = []    # list to hold calculated costs, used to choose minimum
        for x in range(1, t+1):
            breaksCase = self.recursive(p = p - 1, t = x - 1)
            intactCase = self.recursive(p = p, t = t - x)
            maxThrows = max(breaksCase, intactCase)
            results.append(maxThrows)
        results.sort()
        return 1 + results[0]

    def dynamic(self, p: int, t: int):
        self.dynamic_counter += 1
        # TODO
        return self.table[p][t]