global TESTNUM
TESTNUM = 4
#TODO move that somewhere, it's a constant

# Globals used:
# TESTNUM

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)
    
# A single trinary value.
# Possible values are 0, 1, and 2.
# To get name from the number, do:
#     >>> State.reverse_mapping[2]
#     'RED'
# Is actually a number, so mutability does not matter.
State = enum('WHITE', 'YELLOW', 'RED')

global WHITE, YELLOW, RED, STATELIST
WHITE = State.WHITE
YELLOW = State.YELLOW
RED = State.RED
STATELIST = (WHITE, YELLOW, RED)

# Get a new placeholder TruthTable.
# @return TruthTable
def TTplaceholder():
    return TruthTable.placeholder()


# A set of TESTNUM states, one for each tested input.
# Mutable. Serializable.
class WireContents(object):
    # local vars
    # State[] states - the State of the wire for each test
    
    # Constructor
    # initial values are optional
    def __init__(self, initial=None):
        states = [WHITE for i in range(TESTNUM)]
        if initial != None:
            assert(len(initial) == TESTNUM)
            for obj in initial:
                assert(WHITE <= obj <= RED)
            else:
                states = list(initial)
        self.states = states
    
    def __len__(self):
        return TESTNUM
    
    def __getitem__(self, test):
        return self.states[test]
    
    def __setitem__(self, test, val):
        assert(0 <= test < TESTNUM)
        self.states[test] = val
    
    def __iter__(self):
        return self.states.__iter__()
    
    # Get a single value from this wire.
    # @arg test - which test to get the value from
    # @return State
    def getSingle(self, test):
        return self.__getitem__(test)
    
    # Get all values on this wire.
    # @return list(State)
    def getAll(self):
        return self.states
    
    # Set a single value on this wire.
    # @arg test - which test to get the value from
    # @arg val - the new State
    def setSingle(self, test, val):
        self.__setitem__(test, val)
    
    # Set all values on this wire.
    # @arg values - n-list of States
    def setAllState(self, values):
        assert(len(values) == TESTNUM)
        self.states = values
    
    def __delitem__():
        raise NotImplemented
    
    def __reversed__():
        raise NotImplemented
    
    def __contains__():
        raise NotImplemented

# A truth table. Maps inputs to outputs.
# Immutable. Serializable.
class TruthTable (object):
    # local vars
    # State[][] table - the truth table used by this
    #   when reading the table, refer to the following:
    #        RIGHT
    #   L [[WW WY WR]
    #   E  [YW YY YR]
    #   F  [RW RY RR]]
    #   T
    
    # static vars
    # TruthTable _placeholder - truth table of all zeros, intended as placeholder
    
    # Constructor
    # initial values are MANDATORY.
    def __init__(self, values):
        assert(len(values) == len(STATELIST))
        for row in values:
            assert(len(row) == len(STATELIST))
            for i in row:
                assert(WHITE <= i <= RED)
        self.table = values
        self._isPH = False
    
    def __getitem__(self, key):
        return self.table[key[0]][key[1]]
    
    # Get the result from these inputs.
    # @arg left - State on the left
    # @arg right - State on the right
    # @return State
    def getResult(self, left, right):
        return self[left,right]
    
    # Get the result WireContents given these WireContents.
    # @arg left - WireContents on the left
    # @arg right - WireContents on the right
    # @return WireContents
    def getWireResult(self, left, right):
        assert(type(left) == type(right) == WireContents) #this check does work as intended
        return WireContents(self.table[left[i],right[i]] for i in TESTNUM)
    
    # Get a copy of this TruthTable.
    # @return TruthTable
    def clone(self):
        r = TruthTable(table)
        r._isPH = self._isPH
        return r
    
    # Whether this TruthTable shall be considered a placeholder.
    # @return boolean
    def isPlaceholder(self):
        return self._isPH
    
    # Get a new placeholder TruthTable.
    # @return TruthTable - copy of _placeholder
    def placeholder():
        return _placeholder.clone()

TruthTable._placeholder = TruthTable( ((0,0,0), (0,0,0), (0,0,0)) )
TruthTable._placeholder._isPH = True

