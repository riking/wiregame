# Puzzle configuration. Declares the I/O relationship between components.
class PuzzleConfig (dict):
    # local vars
    # str(id) goal - the ident of the goal component
    
    # Constructor
    # first arg should be the goal's ident
    # all other args should be named with the idents
    # other args must be either None or a 2-tuple of idents also present in the list
    def __init__(self, *args, **kwargs):
        # Setup
        assert(len(args) == 1)
        self.goalId = args[0]
        
        # Super
        super(PuzzleConfig, self).__init__(kwargs)
        
        # Format Verification
        names = self.keys()
        for k in self:
            v = kwargs[k]
            if v == None: continue
            assert len(v) == 2 #only two inputs
            if v[0] not in names: raise ValueError("The identifier of "+ v[0] + " used in " + k + " was not defined.")
    
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
    
    def exists(self, ident):
        return ident in self
    
    def getGoal(self):
        return self.goalId

# current default
puzzle = PuzzleConfig('G',
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
    print 'Usage of','B',puzzle.getUsage('B')
    print 'Is input','B',puzzle.isInput('B')
    print 'Goal',repr(puzzle.getGoal())
