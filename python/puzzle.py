import puzzleconfig, wires

import copy, random

# Puzzle holds all the allowed truthtables for this puzzle.
# It holds the output goal, the locked & the extra TruthTable.
# It also holds the PuzzleConfig.
class Puzzle (object):
    # local vars
    # PuzzleConfig config
    # WireContents goal - the desired output at the goal
    # list(TruthTable) allowed - the allowed truth tables
    # TruthTable extra - the extra truth table
    # TruthTable locked_tt - the locked TT
    # str(id) locked_id - the component ident of the locked piece
    
    # Constructor
    def __init__(self, config, goal, tables, extra, locked_tt, locked_id):
        self.config = config
        self.goal = goal
        self.allowed = tables
        self.extra = extra
        self.locked_tt = locked_tt
        self.locked_id = locked_id
        assert(config.exists(locked_id))
        assert(locked_tt in allowed)
        assert(extra not in allowed)
    
    # Returns all truth tables that should show up.
    # @return list
    def getAllowed(self, useExtra):
        l = copy.copy(allowed)
        if useExtra:
            l.add(extra)
        return l
    
    # Returns A SHUFFLED list of truth tables that should start on the sidebar.
    # If useExtra is true, the locked TT is removed and the extra inserted.
    # @return list
    def getMovableTruthTablesShuffled(self, useExtra):
        l = copy.copy(allowed)
        if useExtra:
            l.add(extra)
            l.remove
        return random.shuffle(l)

    # Puts the locked truth table into the proper component, given the board.
    def fillLockedComponent(self, board):
        pass #TODO
    
    # @return TruthTable
    def getLockedTT(self):
        return locked_tt
    
    # @return ident
    def getLockedIdent(self):
        return locked_id
    
    # @return PuzzleConfig
    def getPuzzleConfig(self):
        return config
    
    # @return WireContents
    def getGoalOutput(self):
        return goal
    
    # @return list(ident)
    def getAllIdents(self):
        return config.keys()

