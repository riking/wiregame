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
            assert "SIDE_" not in k # reserved names for sidebar
            v = kwargs[k]
            if v == None: continue
            assert len(v) == 2 #only two inputs
            if v[0] not in self: raise ValueError("The identifier of "+ v[0] + " used in " + k + " was not defined.")
    
    # Whether the specified ident is an input device.
    # @return boolean
    def isInput(self, ident):
        return self[ident] == None
    
    # If the specified ident is not an input device, i.e. its output is calculated.
    # @return boolean
    def isCalculated(self, ident):
        return self[ident] != None
    
    # Get the inputs to this device.
    # If this is an input device, return (None, None).
    # @return 2-tuple (ident,ident)
    def getInputs(self, ident):
        ret = self[ident]
        if ret == None: ret = (None, None)
        return ret
    
    # Get all devices that have this device as an input.
    # @return set(ident)
    def getUsage(self, ident):
        ret = set()
        for id2 in self:
            if self[id2] == None: continue
            if ident in self[id2]:
                ret.add(id2)
        return ret
    
    # Whether the given ident is in this config.
    # @return boolean
    def exists(self, ident):
        return ident in self
    
    # The goal device.
    # @return ident
    def getGoal(self):
        return self.goalId
    
    # All input devices in the circuit.
    # @return set(ident)
    def getAllInputDevices(self):
        ret = set()
        for id2 in self:
            if self[id2] == None:
                ret.add(id2)
        return ret

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
