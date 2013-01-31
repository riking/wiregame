import component, puzzle, wires

# TODO move this somewhere, it's a constant
SIDEBAR_IDENT_PREFIX = "SIDE_"

# The grand container for the state of the game.
# Holds the Puzzle object and a dictionary of all Components by ident.
# Handles swapping of TruthTables and triggering recalcs.
class Board (object):
    # local vars
    # Puzzle puzzle - the puzzle object
    # dict<str(id), Component> components - dictionary of components by ident
    # list<Component> sidebar - components not actually in circuit. hold unused truthtables
    # boolean lock - whether to use the extra & locked components
    
    # static vars
    sidebar_suffix = 0
    
    # Constructor
    # @arg Puzzle puz - Puzzle object
    # @arg boolean lock - whether the extra & locked components are to be used
    def __init__(self, puz, lock):
        self.puzzle = puz
        self.lock = lock
        self._init_sidebar()
        self._init_components()
    
    def _init_sidebar(self):
        self.sidebar = list()
        sidebar_tts = self.puzzle.getMovableTruthTablesShuffled(lock)
        for tt in sidebar_tts:
            newid = SIDEBAR_IDENT_PREFIX + str(sidebar_suffix)
            sidebar_suffix += 1
            comp = component.Component(newid, tt, None) # TODO create render info
            sidebar.append(comp)
    
    def _init_components(self):
        # Create components
        self.components = dict.fromkeys(self.puzzle.getAllIdents())
        for ident in self.components:
            self.components[ident] = component.Component(
              ident, wires.TTplaceholder(), None) # TODO create render info
        
        # Define input relations
        config = self.puzzle.getPuzzleConfig()
        for ident in self.components:
            inputs = config.getInputs(ident)
            self.components[ident].defineInputs(inputs[0], inputs[1])
        
        # Fill input devices
        inputs = config.getAllInputDevices()
        for ident in inputs:
            self.components[ident].setPermanentInput(self.puzzle.getDeviceInput(ident))
        
        # Fill locked component
        if self.lock:
            ident = self.puzzle.getLockedIdent()
            self.components[ident].setTruthTable(self.puzzle.getLockedTT())
    
    def getComponent(self, ident):
        return components[ident]
