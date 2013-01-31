class PuzzleConfig (dict):
    def __init__(self, *args, **kwargs):
        # Format Verification
        names = list()
        for k in kwargs:
            names.append(k)
        for k in kwargs:
            v = kwargs[k]
            if v == None: continue
            if len(v) != 2: raise ValueError("Attempt to use more than 2 inputs in puzzle. More than 2 inputs is not supported.")
            if v[0] not in names: raise ValueError("The identifier of "+ v[0] + " used in " + k + " was not defined.")
        # Constructor
        super(PuzzleConfig, self).__init__(kwargs)
    
    def isInput(self, ident):
        return self[ident] == None
    
    def isCalculated(self, ident):
        tmp = self[ident]
        return type(tmp) == tuple and len(tmp) == 2
    
    def getUsage(self, ident):
        ret = set()
        for c in self:
            if self[c] == None: continue
            if ident in self[c]:
                ret.add(c)
        return ret

# current default
puzzle = PuzzleConfig(
    A=None,
    B=None,
    C=('A','A'),
    D=('C','B'),
    E=('C','D'),
    F=('D','B'),
    G=('E','F') )

# Tests
if __name__ == "__main__":
    print puzzle
    print puzzle.getUsage('C')
    print puzzle.getUsage('A')
