import wires

# A place on the board where wires go through and a truthtable can be inserted.
# Is immutable, but the truth table can change.
# Renderinfo is TODO
class Component (object):
    # local vars
    # str(id) ident - identifier specified by puzzle config
    # object renderinfo - Information for the renderer.
    # str(id) left - the component ident inputting on the left
    # str(id) right - the component ident inputting on the right
    # boolean isInput - whether this Component is an input device in the circuit
    # long timestamp - when lastOut was last updated
    # WireContents lastOut - last computed output from this Component
    
    # Constructor
    # be sure to call defineInputs()
    def __init__(self, ident, truthtable, renderinfo=None):
        self.ident = ident
        self.renderinfo = renderinfo
        self.table = truthtable
        self.timestamp = -1L
        self.lastOut = wires.WireContents()
    
    def defineInputs(self, inleft, inright):
        assert not (inleft==None) ^ (inright==None) # both or neither are none
        self.left = inleft
        self.right = inright
        self.isInput = (inleft == None and inright == None)
    
    def getLastOutput(self):
        return self.lastOut
    
    def setOutput(self, wire, ts):
        self.timestamp = ts
        self.lastOut = wire
    
    def isOutputUpdated(self, ts):
        return self.timestamp == ts
    
    def getOutput(self, ts):
        return self.lastOut if self.isOutputUpdated(ts) else None
    
    def setTruthTable(self, newTT):
        self.table = newTT
    
    def getTruthTable(self):
        return self.table
