import puzzle

# The grand container for the state of the game.
# Holds the Puzzle object and a dictionary of all Components by ident.
# Handles swapping of TruthTables and triggering recalcs.
class Board (object):
    # local vars
    # Puzzle puzzle - the puzzle object
    # dict<str(id), Component> components - dictionary of components by ident
    # list<Component> sidebar - components not actually in circuit. hold unused truthtables
    
    # Constructor
    def __init__(self, puz):
        self.puzzle = puz
        
